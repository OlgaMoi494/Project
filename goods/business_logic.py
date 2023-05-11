from datetime import datetime
from data_access import (
    read_category_data,
    write_category_data,
    read_goods_data,
    write_goods_data,
    max_item_id,
    read_order_data,
    write_order_data,
    max_order_id,
    write_to_excel
)
from errors import IncorrectUserInputError
from validators import decor_validate


def add_category(category):
    data = read_category_data()
    data.append(category)
    write_category_data(data)


def check_name_category(category, name):
    lst_of_match = []
    for item in read_goods_data():
        if item['category'] == category and item['name'] == name:
            lst_of_match.append(item)
    for item in lst_of_match:
        for parameter in item:
            print(f'{parameter}: {item[parameter]}')
        print()
    if lst_of_match:
        return lst_of_match[0]


def update_quantity(item_to_update, quantity):
    new_data = []
    for item in read_goods_data():
        if item == item_to_update:
            item['quantity'] = quantity
            item['updated_at'] = datetime.now().isoformat()
        new_data.append(item)
    write_goods_data(new_data)


def check_category_parameters(category):
    for item in read_category_data():
        for key in item:
            if key == category:
                return item.get(key)


def check_if_item_exists(item_dct):
    share_dct = {}
    for item in read_goods_data():
        for key in item_dct:
            if (key in item) and (item[key] == item_dct[key]):
                share_dct[key] = item_dct[key]

    if share_dct == item_dct:
        return share_dct == item_dct


def create_item(dct_of_parameters):
    if not read_goods_data():
        item_id = '0'
    else:
        item_id = str(max_item_id() + 1)
    item_dct = {}
    item_dct['item_id'] = item_id
    item_dct.update(dct_of_parameters)
    return item_dct


def add_item_parameters(item_dct):
    item_dct['created_at'] = datetime.now().isoformat()
    item_dct['updated_at'] = datetime.now().isoformat()
    data = read_goods_data()
    data.append(item_dct)
    write_goods_data(data)


def lst_of_categories_available():
    lst_of_categories = []
    for i in read_category_data():
        for k in i:
            lst_of_categories.append(k)
    return lst_of_categories


@decor_validate
def validate_category_in_db(value):
    if value not in lst_of_categories_available():
        raise IncorrectUserInputError("The category entered doesn't exist. You"
                                      " can add a new category in the menu.")


@decor_validate
def validate_category_in_db_not_none(value):
    if value not in lst_of_categories_available() and value:
        raise IncorrectUserInputError("The category entered doesn't exist. You"
                                      " can add a new category in the menu.")


@decor_validate
def validate_category_not_in_db(value):
    if value in lst_of_categories_available():
        raise IncorrectUserInputError("The category entered already exists.")


def get_items_by_category(category):
    data = read_goods_data()
    lst_of_items_available = []
    for item in data:
        if item['quantity'] > 0:
            if not category:
                lst_of_items_available.append(item)
            elif item['category'] == category:
                lst_of_items_available.append(item)
    return lst_of_items_available


def items_available_by_dates(lst_of_items_available, min_date, max_date):
    lst_of_items = []
    if not min_date and not max_date:
        for item in lst_of_items_available:
            item_dct = {}
            item_dct['item_id'] = item['item_id']
            item_dct['name'] = item['name']
            lst_of_items.append(item_dct)
    if min_date:
        min_date = datetime.strptime(min_date, '%Y.%m.%d').date()
    if max_date:
        max_date = datetime.strptime(max_date, '%Y.%m.%d').date()
    for item in lst_of_items_available:
        item_dct = {}
        item['created_at'] = datetime.strptime(item['created_at'],
                                               '%Y-%m-%dT%H:%M:%S.%f').date()
        if min_date and not max_date:
            if item['created_at'] >= min_date:
                item_dct['item_id'] = item['item_id']
                item_dct['name'] = item['name']
                lst_of_items.append(item_dct)
        elif not min_date and max_date:
            if item['created_at'] <= max_date:
                item_dct['item_id'] = item['item_id']
                item_dct['name'] = item['name']
                lst_of_items.append(item_dct)
        elif min_date and max_date:
            if max_date >= item['created_at'] >= min_date:
                item_dct['item_id'] = item['item_id']
                item_dct['name'] = item['name']
                lst_of_items.append(item_dct)
    for item in lst_of_items:
        print(item)
    return lst_of_items


def get_info_by_item_id(item_id):
    item_info = {}
    for item in read_goods_data():
        if item['item_id'] == item_id:
            for parameter in item:
                if parameter == item_id:
                    continue
                if parameter == 'quantity':
                    if item.get(parameter) > 0:
                        item_info['in sale'] = 'Available.'
                    else:
                        item_info['in sale'] = 'Out of stock.'
                    continue
                item_info[parameter] = item[parameter]
    for key, value in item_info.items():
        print(str(key) + ': ' + str(value))
    return item_info


def check_order_in_stock(order_dct):
    data = read_goods_data()
    order_confirmed = {}
    for record in data:
        for item in order_dct:
            if record.get('item_id') == item and record.get(
                    'quantity') >= order_dct.get(item):
                record['quantity'] = record.get('quantity') - order_dct.get(
                    item)
                order_confirmed[item] = (record.get('category'),
                                         record.get('name'),
                                         order_dct.get(item),
                                         record.get('price'))
            elif record.get('item_id') == item and record.get(
                    'quantity') < order_dct.get(item):
                order_confirmed[item] = (
                    record.get('category'), record.get('name'),
                    record.get('quantity'),
                    record.get('price'))
                record['quantity'] = 0
    write_goods_data(data)
    return order_confirmed


def create_order_confirmed(order_confirmed_dct):
    if not order_confirmed_dct:
        return
    order_id_dct = {}
    if not read_order_data():
        order_id = '0'
    else:
        order_id = str(max_order_id() + 1)
    order_id_dct['order_id'] = order_id
    order_id_dct['order'] = order_confirmed_dct
    order_amount = 0
    for key, value in order_confirmed_dct.items():
        order_amount += (value[2] * value[3])
    order_id_dct['order_amount'] = order_amount
    order_id_dct['created_at'] = datetime.now().isoformat()
    data = read_order_data()
    data.append(order_id_dct)
    write_order_data(data)


def select_orders_by_period(min_date, max_date):
    if min_date:
        min_date = datetime.strptime(min_date, '%Y.%m.%d').date()
    if max_date:
        max_date = datetime.strptime(max_date, '%Y.%m.%d').date()
    selected_orders = []
    for order in read_order_data():
        order["created_at"] = datetime.strptime(order['created_at'],
                                                '%Y-%m-%dT%H:%M:%S.%f').date()
        if not min_date and not max_date:
            selected_orders.append(order)
        elif min_date and not max_date:
            if order["created_at"] >= min_date:
                selected_orders.append(order)
        elif not min_date and max_date:
            if order["created_at"] <= max_date:
                selected_orders.append(order)
        elif min_date and max_date:
            if min_date <= order["created_at"] <= max_date:
                selected_orders.append(order)
    return selected_orders


def stat_by_categories_period(min_date, max_date):
    orders_selected = select_orders_by_period(min_date, max_date)
    sales_by_category = []
    for category in read_category_data():
        for key_cat in category:
            category_row = []
            category_quantity_sold = 0
            category_amount_sold = 0

            for order in orders_selected:
                for key, value in order.get('order').items():
                    if value[0] == key_cat:
                        category_quantity_sold += value[2]
                        amount_sold = value[2] * value[3]
                        category_amount_sold += amount_sold
            category_row.append(key_cat)
            category_row.append(category_quantity_sold)
            category_row.append(category_amount_sold)
            sales_by_category.append(category_row)

    return sales_by_category


def items_quantity_sold_period(min_date, max_date):
    orders_selected = select_orders_by_period(min_date, max_date)
    sold_item = {}
    for order in orders_selected:
        for item_id, value in order.get('order').items():
            item_tuple = (item_id, value[1])
            if item_tuple in sold_item:
                sold_item[item_tuple] = (
                    sold_item[item_tuple][0] + value[2],
                    sold_item[item_tuple][1] + (value[2] * value[3]))
            else:
                sold_item[item_tuple] = (value[2], value[3] * value[2])

    items_sold_lst = []
    for key, value in sold_item.items():
        lst = []
        lst.append(key[0])
        lst.append(key[1])
        lst.append(value[0])
        lst.append(value[1])
        items_sold_lst.append(lst)
    return items_sold_lst


def lst_orders_period(min_date, max_date):
    orders_selected = select_orders_by_period(min_date, max_date)
    orders_lst = []
    for order in orders_selected:
        current_order = []
        current_order.append(order.get('order_id'))
        current_order.append(order.get('order_amount'))
        current_order.append(order.get('created_at'))
        orders_lst.append(current_order)

    orders_lst.sort(key=lambda x: x[1], reverse=True)
    return orders_lst


def popular_category_period(min_date, max_date):
    orders_selected = select_orders_by_period(min_date, max_date)
    category_in_orders_count = {}
    for category in read_category_data():
        for key_category in category:
            category_counter = 0
            for order in orders_selected:
                for item in order.get('order'):
                    if key_category in order.get('order').get(item):
                        category_counter += 1
                        category_in_orders_count[
                            key_category] = category_counter

    category_in_orders_count = sorted(category_in_orders_count.items(),
                                      key=lambda x: x[1], reverse=True)
    the_most_popular_category = category_in_orders_count[0][0]
    return the_most_popular_category


def most_popular_item(min_date, max_date):
    orders_selected = select_orders_by_period(min_date, max_date)
    item_in_orders = {}
    for order in orders_selected:
        for item_id, value in order.get('order').items():
            item_tuple = (item_id, value[1])
            if item_tuple in item_in_orders:
                item_in_orders[item_tuple] += 1
            else:
                item_in_orders[item_tuple] = 1

    item_in_orders = sorted(item_in_orders.items(), key=lambda x: x[1],
                            reverse=True)
    most_popular_item = item_in_orders[0][0][1]
    return most_popular_item


def total_quantity_amount(min_date, max_date):
    orders_selected = select_orders_by_period(min_date, max_date)
    total_revenue = 0
    total_item_id_sold = set()
    for order in orders_selected:
        total_revenue += order.get('order_amount')
        for item in order.get('order'):
            total_item_id_sold.add(item)
    number_of_goods_sold = len(total_item_id_sold)
    return (total_revenue, number_of_goods_sold)


def statistics(sh1, sh2, sh3, sh4, min_date, max_date):
    write_to_excel(sh1, sh2, sh3, sh4, min_date, max_date)
