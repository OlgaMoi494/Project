import csv
from statistics import mean

with open('sp500.csv', newline='') as sp_file:
    reader = csv.DictReader(sp_file)
    data = list(reader)

cache_dct = {}


def cache_check(function):
    def wrapper(search_item: str, *args, **kwargs):
        if search_item in cache_dct:
            return cache_dct[search_item]
        else:
            return function(search_item, *args, **kwargs)

    return wrapper


def company_info_dct(lst_entry: dict) -> dict:
    select_company_dict = {}
    select_company_dict['Name'] = (lst_entry['Name'])
    select_company_dict['Symbol'] = (lst_entry['Symbol'])
    select_company_dict['Sector'] = (lst_entry['Sector'])
    select_company_dict['Stock price'] = (lst_entry['Price'])
    return select_company_dict


@cache_check
def info_by_name(search_item: str, source_lst: list) -> list:
    '''Returns list of company dicts selected by name'''
    lst_of_companies_selected = []
    for item in source_lst:
        if search_item in item['Name'].lower():
            lst_of_companies_selected.append(company_info_dct(item))
    print(f'Companies selected by name: {lst_of_companies_selected}')
    return lst_of_companies_selected


@cache_check
def info_by_symbol(search_item: str, source_lst: list) -> list:
    '''Returns list of company dicts selected by symbol'''
    lst_of_companies_selected_by_symbol = []
    for item in source_lst:
        if search_item in item['Symbol'].lower():
            lst_of_companies_selected_by_symbol.append(company_info_dct(item))
    print(
        f'Companies selected by symbol: {lst_of_companies_selected_by_symbol}')
    return lst_of_companies_selected_by_symbol


@cache_check
def info_by_sector(search_item: str, source_lst: list) -> list:
    '''Returns list of company names selected by sector'''
    lst_of_companies_selected_by_sector = []
    for item in source_lst:
        if search_item in item['Sector'].lower():
            lst_of_companies_selected_by_sector.append(item['Name'])
    print(
        f'Companies selected by sector: {lst_of_companies_selected_by_sector}')
    return lst_of_companies_selected_by_sector


def average_price(source_lst: list) -> float:
    '''Returns average stock price of all the companies'''
    prices = []
    for i in source_lst:
        prices.append(float(i['Price']))
    print(f'Average stock price of the companies: {round(mean(prices), 2)}')
    return mean(prices)


def top10_companies(source_lst: list) -> list:
    '''Returns top10 companies ranged on stock price'''
    prices = []
    names = []
    for i in source_lst:
        prices.append(float(i['Price']))
        names.append(i['Name'])
    companies_prices_lst = list(zip(names, prices))
    companies_prices_lst_sorted = sorted(companies_prices_lst,
                                         key=lambda tpl: tpl[1], reverse=True)
    companies_prices_lst_top10 = companies_prices_lst_sorted[:10]
    print(f'Top 10 companies on stock price: {companies_prices_lst_top10}')
    return companies_prices_lst_top10


def main_program() -> None:
    '''Performs main menu console program'''
    while True:
        print('Choose the action from menu \n\
    1 - Find info by name\n\
    2 - Find info by symbol\n\
    3 - Get all companies by sector\n\
    4 - Calculate average price\n\
    5 - Get top 10 companies\n\
    6 - Exit\n')
        your_choice = int(input('Your choice: '))
        if your_choice == 1:
            name = input('Enter the name of company: ').lower()
            result = info_by_name(name, data)
            cache_dct[name] = result
        elif your_choice == 2:
            symbol = input('Enter the symbol of company: ').lower()
            result = info_by_symbol(symbol, data)
            cache_dct[symbol] = result
        elif your_choice == 3:
            sector = input('Enter the sector for search: ').lower()
            result = info_by_sector(sector, data)
            cache_dct[sector] = result
        elif your_choice == 4:
            average_price(data)
        elif your_choice == 5:
            top10_companies(data)
        elif your_choice == 6:
            print('GOODBYE')
            break
        else:
            print('Please correct your choice')
            continue
    print(f'Cache dict: {cache_dct}')


main_program()
