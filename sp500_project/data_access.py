import csv
import json
import os
from abc import ABC, abstractmethod


class IStorage(ABC):
    @abstractmethod
    def read_data(self):
        raise NotImplementedError

    @abstractmethod
    def read_headers(self):
        raise NotImplementedError

    @abstractmethod
    def read_lst_of_symbols(self) -> list:
        raise NotImplementedError

    @abstractmethod
    def read_lst_of_names(self) -> list:
        raise NotImplementedError

    @abstractmethod
    def read_lst_of_sectors(self) -> set:
        raise NotImplementedError

    @abstractmethod
    def write_new_company(self, new_company_entry: list):
        raise NotImplementedError

    @abstractmethod
    def write_updates(self, update_name_entry: dict):
        raise NotImplementedError

    @abstractmethod
    def rewrite_from_temp_file(self):
        raise NotImplementedError

    @abstractmethod
    def write_delete_company(self, entry_to_delete: list) -> None:
        raise NotImplementedError

    @abstractmethod
    def clear_the_data(self):
        raise NotImplementedError

    @abstractmethod
    def write_random_data(self, headers: list,
                          full_lst_of_entries: list[list]):
        raise NotImplementedError


class CSVStorage(IStorage):
    def __init__(self, file_name):
        self.file_name = file_name

    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value: str):
        if value.split('.')[1] != 'csv':
            raise ValueError("Invalid file extension.")

        self._file_name = value

    def read_data(self):
        with open(self.file_name, newline='') as sp_file:
            return list(item for item in csv.DictReader(sp_file))

    def read_headers(self):
        with open(self.file_name) as sp_file:
            return csv.DictReader(sp_file).fieldnames

    def read_lst_of_symbols(self) -> list:
        with open(self.file_name, newline='') as sp_file:
            return [item['Symbol'] for item in csv.DictReader(sp_file)]

    def read_lst_of_names(self) -> list:
        with open(self.file_name, newline='') as sp_file:
            return [item['Name'] for item in csv.DictReader(sp_file)]

    def read_lst_of_sectors(self) -> set:
        with open(self.file_name, newline='') as sp_file:
            return set(item['Sector'] for item in csv.DictReader(sp_file))

    def write_new_company(self, new_company_entry: list):
        with open(self.file_name, 'a', newline='') as sp_file:
            writer = csv.writer(sp_file)
            writer.writerow(
                new_company_entry)
        self.read_data()

    def write_updates(self, update_name_entry: dict):
        with open(self.file_name, 'r') as sp_file:
            reader = csv.DictReader(sp_file)
            with open(self.file_name + '1', 'w', newline='') as sp1_file:
                writer = csv.DictWriter(sp1_file, fieldnames=reader.fieldnames)
                writer.writeheader()
                for i in reader:
                    if i.get('Symbol') == update_name_entry.get('Symbol'):
                        writer.writerow(update_name_entry)
                    else:
                        writer.writerow(i)

    def rewrite_from_temp_file(self):
        with open(self.file_name + '1') as sp1_file:
            reader = csv.DictReader(sp1_file)
            with open(self.file_name, 'w', newline='') as sp_file:
                writer = csv.DictWriter(sp_file, fieldnames=reader.fieldnames)
                writer.writeheader()
                for i in reader:
                    writer.writerow(i)
        if os.path.exists(self.file_name + '1'):
            os.remove(self.file_name + '1')
        self.read_data()

    def write_delete_company(self, entry_to_delete: list) -> None:
        with open(self.file_name + '1', 'w', newline='') as sp1_file:
            fieldnames = self.read_headers()
            writer = csv.DictWriter(sp1_file, fieldnames=fieldnames)
            writer.writeheader()
            for row in self.read_data():
                if row == entry_to_delete:
                    continue
                else:
                    writer.writerow(row)

    def clear_the_data(self):
        with open(self.file_name, 'w'):
            pass

    def write_random_data(self, headers: list,
                          full_lst_of_entries: list[list]):
        with open(self.file_name, 'w', newline='') as w_sp_file:
            writer = csv.writer(w_sp_file)
            writer.writerow(headers)
            writer.writerows(full_lst_of_entries)


class JSONStorage(IStorage):
    def __init__(self, file_name):
        self.file_name = file_name

    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value: str):
        if value.split('.')[1] != 'json':
            raise ValueError("Invalid file extension.")

        self._file_name = value

    def read_data(self):
        with open(self.file_name, newline='') as sp_file:
            return json.load(sp_file)

    def read_headers(self):
        with open(self.file_name) as sp_file:
            return list(json.load(sp_file)[0].keys())

    def read_lst_of_symbols(self) -> list:
        with open(self.file_name, newline='') as sp_file:
            return [item['Symbol'] for item in json.load(sp_file)]

    def read_lst_of_names(self) -> list:
        with open(self.file_name, newline='') as sp_file:
            return [item['Name'] for item in json.load(sp_file)]

    def read_lst_of_sectors(self) -> set:
        with open(self.file_name, newline='') as sp_file:
            return set(item['Sector'] for item in json.load(sp_file))

    def write_new_company(self, new_company_entry: list):
        with open(self.file_name) as sp_file:
            data = json.load(sp_file)
            headers = list(data[0].keys())
            new_entry = {headers[index]: item for index, item in
                         enumerate(new_company_entry)}
            data.append(new_entry)
            with open(self.file_name, 'w') as sp_file:
                json.dump(data, sp_file)

    def write_updates(self, update_name_entry: dict):
        with open(self.file_name, 'r') as sp_file:
            data = json.load(sp_file)
            new_data = []
            for i in data:
                if i.get('Symbol') == update_name_entry.get('Symbol'):
                    new_data.append(update_name_entry)
                else:
                    new_data.append(i)
            with open(self.file_name + '1', 'w') as sp1_file:
                json.dump(new_data, sp1_file)

    def rewrite_from_temp_file(self):
        with open(self.file_name + '1') as sp1_file:
            reader = json.load(sp1_file)
            with open(self.file_name, 'w', newline='') as sp_file:
                json.dump(reader, sp_file)
        if os.path.exists(self.file_name + '1'):
            os.remove(self.file_name + '1')

    def write_delete_company(self, entry_to_delete: list) -> None:
        with open(self.file_name + '1', 'w', newline='') as sp1_file:
            new_data = []
            for row in self.read_data():
                if row == entry_to_delete:
                    continue
                else:
                    new_data.append(row)
            json.dump(new_data, sp1_file)

    def clear_the_data(self):
        with open(self.file_name, 'w'):
            pass

    def write_random_data(self, headers: list,
                          full_lst_of_entries: list[list]):
        new_data = [dict(zip(headers, entry)) for entry in full_lst_of_entries]
        with open(self.file_name, 'w', newline='') as w_sp_file:
            json.dump(new_data, w_sp_file)
