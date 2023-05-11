from validators import (
    validate_user_choice,
    validate_item_quantity
)
from business_logic import (
    add_category,
    lst_of_categories_available,
    create_item,
    add_item_parameters,
    validate_category_in_db,
    validate_category_not_in_db,
    validate_category_in_db_not_none,
    get_items_by_category,
    items_available_by_dates,
    check_category_parameters,
    check_name_category,
    update_quantity,
    get_info_by_item_id,
    check_order_in_stock,
    create_order_confirmed,
    stat_by_categories_period,
    items_quantity_sold_period,
    lst_orders_period,
    total_quantity_amount,
    popular_category_period,
    most_popular_item,
    statistics
)


def main_program():
    while True:
        print('Choose the action from menu: \n'
              '1 - Create a new category.\n'
              '2 - Add a new product.\n'
              '3 - Get all goods in stock.\n'
              '4 - Get a chosen product.\n'
              '5 - Make an order.\n'
              '6 - Get Statistics.\n'
              '7 - Exit.')
        while True:
            your_choice = input('Your choice: ')
            if validate_user_choice(your_choice):
                break
        if your_choice == '7':
            break

        elif your_choice == '1':
            print(f'Categories available: '
                  f'{lst_of_categories_available()}')
            while True:
                category_name = input(
                    'Create a new category(enter "n" to quite): ')
                if validate_category_not_in_db(category_name):
                    break
                if category_name == 'n':
                    break
            if category_name == 'n':
                continue
            category_dct = {}
            category_attributes = ['name', 'price']
            print(f'Attributes by default: {category_attributes}')
            while True:
                attribute = input(
                    'Create a new attribute("n" to quit): ')
                if attribute.lower() == 'n':
                    break
                category_attributes.append(attribute)
            category_dct[category_name] = category_attributes
            add_category(category_dct)

        elif your_choice == '2':
            while True:
                print(f'Categories available: '
                      f'{lst_of_categories_available()}')

                category = input(
                    'Please enter a category from the list (Enter "n" for '
                    'back menue): ').lower()
                if category == 'n':
                    break
                if validate_category_in_db(category):
                    break
            if category == 'n':
                continue
            while True:
                name = input('Please enter the name: ').capitalize()
                existing_item = check_name_category(category, name)
                if not existing_item:
                    break
                else:
                    match_name = input(
                        '1 - update the quantity to the existing '
                        'item;\n'
                        '2 - to to create a new '
                        'item;\n\n'
                        'Please choose the option: ')
                    if match_name == '1':
                        new_quantity = input('Please enter a new quantity: ')
                        new_quantity = int(new_quantity)
                        update_quantity(existing_item, new_quantity)
                        break
                    elif match_name == '2':
                        continue
            if existing_item:
                continue
            else:
                lst_of_parameters = check_category_parameters(category)
                parameters_dct = {}
                parameters_dct["category"] = category
                parameters_dct["name"] = name
                for parameter in lst_of_parameters:
                    if parameter == 'name':
                        continue
                    parameters_dct[parameter] = input(
                        f'Enter {parameter}: ').lower()
                    if parameter == 'price':
                        parameters_dct[parameter] = float(
                            parameters_dct[parameter])
                parameters_dct = create_item(parameters_dct)
                while True:
                    parameters_dct['quantity'] = input(
                        'Enter quantity available: ')
                    if validate_item_quantity(parameters_dct['quantity']):
                        break
                parameters_dct['quantity'] = int(parameters_dct['quantity'])
                add_item_parameters(parameters_dct)

        elif your_choice == '3':
            print(f'Categories available: '
                  f'{lst_of_categories_available()}')
            while True:
                category = input('Please enter the category: ').lower()
                if validate_category_in_db_not_none(category):
                    break
            min_add_date = input('Please enter min date of item adding'
                                 'in format "yyyy.mm.dd":')
            max_add_date = input('Please enter max date of item adding'
                                 'in format "yyyy.mm.dd":')
            lst_of_items_available = get_items_by_category(category)
            items_available_by_dates(lst_of_items_available, min_add_date,
                                     max_add_date)

        elif your_choice == '4':
            item_id = input('Please enter the item_id: ')
            get_info_by_item_id(item_id)

        elif your_choice == '5':
            order_dct = {}

            while True:
                item_id_ordered = input('Enter item id(n to quit): ')
                if item_id_ordered == 'n':
                    break
                quantity_ordered = input('Enter quantity ordered(n to quit): ')
                if quantity_ordered == 'n':
                    break
                quantity_ordered = int(quantity_ordered)
                order_dct[item_id_ordered] = quantity_ordered
            order_confirmed = check_order_in_stock(order_dct)
            create_order_confirmed(order_confirmed)

        elif your_choice == '6':
            min_add_date = input('Please enter min date of item adding'
                                 'in format "yyyy.mm.dd":')
            max_add_date = input('Please enter max date of item adding'
                                 'in format "yyyy.mm.dd":')
            sh1 = stat_by_categories_period(min_add_date, max_add_date)
            sh2 = items_quantity_sold_period(min_add_date, max_add_date)
            sh3 = lst_orders_period(min_add_date, max_add_date)
            sh4_tuple = (total_quantity_amount(min_add_date, max_add_date),
                         popular_category_period(min_add_date, max_add_date),
                         most_popular_item(min_add_date, max_add_date))
            sh4 = sh4_tuple
            statistics(sh1, sh2, sh3, sh4, min_add_date, max_add_date)


main_program()
