from business_logic import (
    info_by_name,
    info_by_symbol,
    info_by_sector,
    average_price,
    top10_companies,
    validate_symbol_in_db,
    validate_symbol_not_in_db,
    validate_name_not_in_db,
    validate_sector_input,
    cache_dct,
    add_new_company,
    update_name,
    delete_company,
    truncate_all,
    random_data
)
from validators import (
    validate_user_choice,
    validate_symbol_input,
    validate_name_input,
    validate_price,
    validate_number_of_entries
)
from providers import provide_db
from config import DB_FILE, DB_TYPE


def main_program() -> None:
    '''Performs main menu console program'''

    while True:
        print('Choose the action from menu \n\
    1 - Find info by name\n\
    2 - Find info by symbol\n\
    3 - Get all companies by sector\n\
    4 - Calculate average price\n\
    5 - Get top 10 companies\n\
    6 - Add new company\n\
    7 - Update company name\n\
    8 - Delete company\n\
    9 - Truncate all\n\
    10 - Populate file with random data\n\
    11 - Exit\n')
        while True:
            your_choice = input('Your choice: ')
            if validate_user_choice(your_choice):
                break

        if your_choice == '1':
            name = input('Enter the name of company: ').lower()
            info_by_name(name, provide_db(DB_TYPE, DB_FILE))
        elif your_choice == '2':
            symbol = input('Enter the symbol of company: ').lower()
            info_by_symbol(symbol, provide_db(DB_TYPE, DB_FILE))
        elif your_choice == '3':
            print(
                f'List of sectors available: '
                f'{provide_db(DB_TYPE, DB_FILE).read_lst_of_sectors()}')
            sector = input('Enter the sector for search: ').lower()
            info_by_sector(sector, provide_db(DB_TYPE, DB_FILE))
        elif your_choice == '4':
            average_price(provide_db(DB_TYPE, DB_FILE))
        elif your_choice == '5':
            top10_companies(provide_db(DB_TYPE, DB_FILE))
        elif your_choice == '6':
            while True:
                symbol = input(
                    'Please enter symbol(min 3 - max 6 characters):\n').upper()
                if validate_symbol_input(symbol):
                    if validate_symbol_not_in_db(symbol,
                                                 provide_db(DB_TYPE, DB_FILE)):
                        break
            while True:
                name = input(
                    'Please enter name(min 3 - max 50 characters):\n').title()
                if validate_name_input(name, provide_db(DB_TYPE, DB_FILE)):
                    if validate_name_not_in_db(name,
                                               provide_db(DB_TYPE, DB_FILE)):
                        break
            while True:
                print('Please enter sector(choose from the database)')
                for single_sector in provide_db(DB_TYPE,
                                                DB_FILE).read_lst_of_sectors():
                    print(single_sector)
                sector = input('Sector: ').title()
                if validate_sector_input(sector, provide_db(DB_TYPE, DB_FILE)):
                    break
            while True:
                price = input('Please enter price:\n')
                if validate_price(price):
                    break
            add_new_company(symbol, name, sector, price,
                            provide_db(DB_TYPE, DB_FILE))
        elif your_choice == '7':
            while True:
                symbol = input(
                    'Please enter full symbol of the company updated: '
                ).upper()
                if validate_symbol_in_db(symbol, provide_db(DB_TYPE, DB_FILE)):
                    break
            while True:
                new_name = input(
                    'Enter a new name: ').title()
                if validate_name_not_in_db(new_name,
                                           provide_db(DB_TYPE, DB_FILE)):
                    break
            update_name(symbol, new_name, provide_db(DB_TYPE, DB_FILE))
        elif your_choice == '8':
            while True:
                symbol = input(
                    'Please enter the symbol of the company deleted: ').upper()
                if validate_symbol_in_db(symbol, provide_db(DB_TYPE, DB_FILE)):
                    break
            delete_company(symbol, provide_db(DB_TYPE, DB_FILE))
        elif your_choice == '9':
            truncate_all(provide_db(DB_TYPE, DB_FILE))

        elif your_choice == '10':
            while True:
                number_of_entries = input(
                    'Please enter the number of entries to create: ')
                if validate_number_of_entries(number_of_entries):
                    break
            random_data(number_of_entries, provide_db(DB_TYPE, DB_FILE))
            print(f'Data in number of {number_of_entries} entries created!')
        elif your_choice == '11':
            print('GOODBYE')
            break

    print(f'Cache dict: {cache_dct}')


main_program()
