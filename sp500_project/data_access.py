import csv
import os


def read_data():
    with open('sp500.csv', newline='') as sp_file:
        for item in csv.DictReader(sp_file):
            yield item


def read_headers():
    with open('sp500.csv', newline='') as sp_file:
        return csv.DictReader(sp_file).fieldnames


def read_lst_of_symbols() -> list:
    with open('sp500.csv', newline='') as sp_file:
        return [item['Symbol'] for item in csv.DictReader(sp_file)]


def read_lst_of_names() -> list:
    with open('sp500.csv', newline='') as sp_file:
        return [item['Name'] for item in csv.DictReader(sp_file)]


def read_lst_of_sectors() -> set:
    with open('sp500.csv', newline='') as sp_file:
        return set(item['Sector'] for item in csv.DictReader(sp_file))


def write_new_company(new_company_entry: list):
    with open('sp500.csv', 'a', newline='') as sp_file:
        writer = csv.writer(sp_file)
        writer.writerow(
            new_company_entry)
    read_data()


def write_updates(update_name_entry: dict):
    with open('sp500.csv', 'r') as sp_file:
        reader = csv.DictReader(sp_file)
        with open('sp500.csv1', 'w', newline='') as sp1_file:
            writer = csv.DictWriter(sp1_file, fieldnames=reader.fieldnames)
            writer.writeheader()
            for i in reader:
                if i.get('Symbol') == update_name_entry.get('Symbol'):
                    writer.writerow(update_name_entry)
                else:
                    writer.writerow(i)


def rewrite_from_temp_file():
    with open('sp500.csv1') as sp1_file:
        reader = csv.DictReader(sp1_file)
        with open('sp500.csv', 'w', newline='') as sp_file:
            writer = csv.DictWriter(sp_file, fieldnames=reader.fieldnames)
            writer.writeheader()
            for i in reader:
                writer.writerow(i)
    if os.path.exists('sp500.csv1'):
        os.remove('sp500.csv1')
    read_data()


def write_delete_company(entry_to_delete):
    with open('sp500.csv1', 'w', newline='') as sp1_file:
        fieldnames = read_headers()
        writer = csv.DictWriter(sp1_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in read_data():
            if row == entry_to_delete:
                continue
            else:
                writer.writerow(row)


def clear_the_data():
    with open('sp500.csv', 'w'):
        pass


def write_random_data(headers, full_lst_of_entries):
    with open('sp500.csv', 'w', newline='') as w_sp_file:
        writer = csv.writer(w_sp_file)
        writer.writerow(headers)
        writer.writerows(full_lst_of_entries)
