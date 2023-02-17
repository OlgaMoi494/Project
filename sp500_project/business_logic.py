from statistics import mean
from faker import Faker
import random
import string
from time import time
from data_access import (
    read_data,
    read_lst_of_symbols,
    read_lst_of_names,
    read_lst_of_sectors,
    write_new_company,
    write_updates,
    rewrite_from_temp_file,
    write_delete_company,
    clear_the_data,
    write_random_data
)
from errors import IncorrectUserInputError
from validators import decor_validate

cache_dct = {}


def cache_check(storage_time_sec=30):
    def inner(function):
        def wrapper(search_item: str, *args, **kwargs):
            temp_dict = {}
            global cache_dct
            for key, value in cache_dct.items():
                expire_time = value[1] + storage_time_sec
                if expire_time > time():
                    temp_dict[key] = value
            cache_dct = temp_dict
            if search_item in cache_dct:
                print('There are cache data provided!')
                print(cache_dct[search_item][0])
                return cache_dct[search_item][0]
            else:
                return function(search_item, *args, **kwargs)
        return wrapper
    return inner


def company_info_dct(dct_entry: dict) -> dict:
    select_company_dict = {}
    select_company_dict['Name'] = dct_entry.get('Name')
    select_company_dict['Symbol'] = dct_entry.get('Symbol')
    select_company_dict['Sector'] = dct_entry.get('Sector')
    select_company_dict['Stock price'] = dct_entry.get('Price')
    return select_company_dict


@cache_check(30)
def info_by_name(search_item: str) -> list:
    '''Returns list of company dicts selected by name'''
    lst_of_companies_selected = []
    for item in read_data():
        if search_item in item['Name'].lower():
            lst_of_companies_selected.append(company_info_dct(item))
    print(f'Companies selected by name: {lst_of_companies_selected}')
    cache_dct[search_item] = (lst_of_companies_selected, time())
    return lst_of_companies_selected


@cache_check(30)
def info_by_symbol(search_item: str) -> list:
    '''Returns list of company dicts selected by symbol'''
    lst_of_companies_selected_by_symbol = []
    for item in read_data():
        if search_item in item['Symbol'].lower():
            lst_of_companies_selected_by_symbol.append(company_info_dct(item))
    print(
        f'Companies selected by symbol: {lst_of_companies_selected_by_symbol}')
    cache_dct[search_item] = (lst_of_companies_selected_by_symbol, time())
    return lst_of_companies_selected_by_symbol


@cache_check(30)
def info_by_sector(search_item: str) -> list:
    '''Returns list of company names selected by sector'''
    lst_of_companies_selected_by_sector = []
    for item in read_data():
        if search_item in item['Sector'].lower():
            lst_of_companies_selected_by_sector.append(item['Name'])
    print(
        f'Companies selected by sector: {lst_of_companies_selected_by_sector}')
    cache_dct[search_item] = (lst_of_companies_selected_by_sector, time())
    return lst_of_companies_selected_by_sector


def average_price() -> float:
    '''Returns average stock price of all the companies'''
    prices = []
    for i in read_data():
        prices.append(float(i['Price']))
    print(f'Average stock price of the companies: {round(mean(prices), 2)}')
    return mean(prices)


def top10_companies() -> list:
    '''Returns top10 companies ranged on stock price'''
    prices = []
    names = []
    for i in read_data():
        prices.append(float(i['Price']))
        names.append(i['Name'])
    companies_prices_lst = list(zip(names, prices))
    companies_prices_lst_sorted = sorted(companies_prices_lst,
                                         key=lambda tpl: tpl[1], reverse=True)
    companies_prices_lst_top10 = companies_prices_lst_sorted[:10]
    print(f'Top 10 companies on stock price: {companies_prices_lst_top10}')
    return companies_prices_lst_top10


@decor_validate
def validate_symbol_not_in_db(check_input):
    if check_input in read_lst_of_symbols():
        raise IncorrectUserInputError('Symbol entered already exists.')


@decor_validate
def validate_symbol_in_db(check_input):
    if check_input not in read_lst_of_symbols():
        raise IncorrectUserInputError('No symbol entered found.')


@decor_validate
def validate_name_not_in_db(check_input):
    if check_input in read_lst_of_names():
        raise IncorrectUserInputError('Company name entered already exists.')


@decor_validate
def validate_sector_input(check_input):
    if check_input not in read_lst_of_sectors():
        raise IncorrectUserInputError("Sector entered doesn't exist.")


def add_new_company(symbol, name, sector, price):
    new_company_entry = [symbol, name, sector, price] + [None] * 10
    write_new_company(new_company_entry)
    print(
        f'Added new company: symbol: {symbol}, name: {name},'
        f'sector: {sector}, price: {price}')


def update_name(symbol, new_name):
    filter_elem = list(filter(lambda x: x['Symbol'] == symbol, read_data()))[0]
    print(filter_elem)
    filter_elem['Name'] = new_name
    write_updates(filter_elem)
    rewrite_from_temp_file()
    print(filter_elem)
    print('The name is updated in DataBase')


def delete_company(symbol):
    entry_to_delete = list(filter(
        lambda x: x['Symbol'] == symbol, read_data()))[0]
    write_delete_company(entry_to_delete)
    rewrite_from_temp_file()
    print('Selected entry was deleted.')


def truncate_all():
    clear_the_data()
    print('All data cleared!')


def random_data(number_of_entries):
    number_of_entries = int(number_of_entries)
    unique_sectors = ['Telecommunication Services', 'Utilities', 'Energy',
                      'Information Technology', 'Health Care', 'Industrials',
                      'Consumer Staples', 'Consumer Discretionary',
                      'Real Estate',
                      'Financials', 'Materials']
    max_stock_price = 1806.06
    min_stock_price = 2.82
    headers = ['Symbol', 'Name', 'Sector', 'Price', 'Price/Earnings',
               'Dividend Yield', 'Earnings/Share', '52 Week Low',
               '52 Week High',
               'Market Cap', 'EBITDA', 'Price/Sales', 'Price/Book',
               'SEC Filings']
    symbols = [''.join(
        [random.choice(string.ascii_letters),
         random.choice(string.ascii_letters),
         random.choice(string.ascii_letters)]).upper() for _ in
               range(number_of_entries)]
    faker = Faker()
    names = [faker.company() for _ in range(number_of_entries)]
    sectors = [random.choice(unique_sectors) for _ in range(number_of_entries)]
    prices = [str(round(random.uniform(min_stock_price, max_stock_price), 2))
              for _
              in
              range(number_of_entries)]
    lst_nones = [None for _ in range(10)]
    lst_of_entries = list(map(list, zip(symbols, names, sectors, prices)))
    full_lst_of_entries = []
    for i in lst_of_entries:
        i.extend(lst_nones)
        full_lst_of_entries.append(i)
    write_random_data(headers, full_lst_of_entries)
