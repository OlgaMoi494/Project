import random
from data_access import read_names, read_surnames


class PhoneProvider:
    def __call__(self):
        return '(+375)' + '-' + str(random.randint(100, 999)) + '-' + str(
            random.randint(10, 99)) \
               + '-' + str(random.randint(10, 99))


class BankCardProvider:
    def __call__(self):
        sum_digits_processed = 0
        while sum_digits_processed % 10 != 0 or sum_digits_processed == 0:
            sum_digits_processed = 0
            card_number = [random.randint(0, 9) for _ in range(15)]
            card_number.insert(0, random.randint(4, 5))
            for index, digit in enumerate(card_number):
                if index % 2 == 0:
                    digit *= 2
                    if digit > 9:
                        digit -= 9
                sum_digits_processed += digit
                card_number = ''.join(map(str, card_number))
        return f'{card_number[:4]} {card_number[4:8]} {card_number[8:12]} ' \
               f'{card_number[12:]}'


class NameProvider:
    def __call__(self):
        self.name = random.choice(read_names())
        return self.name


class EmailProvider:
    def __init__(self):
        self.valid_chars = 'abcdefghijklmnopqrstuvwxyz1234567890._'

    def __call__(self):
        self.name = random.choice(read_names())
        self.surname = random.choice(read_surnames())
        len_of_login = random.randint(4, 15)
        email_login = ''.join(
            random.choice(self.valid_chars) for _ in range(len_of_login))
        servers = ['@gmail.com', '@yahoo.com', '@yandex.ru', '@hotmail.com',
                   '@mail.ru']
        emails = []
        full_email = email_login + random.choice(servers)
        full_email1 = random.choice(
            self.valid_chars[:self.valid_chars.find('1')]) + "." + \
            self.surname + random.choice(servers)
        full_email2 = self.name + "_" + self.surname + random.choice(
            servers)
        full_email3 = self.name + str(
            random.randint(1955, 2010)) + random.choice(servers)
        full_email4 = self.name + "_" + random.choice(
            self.valid_chars) + random.choice(
            servers)
        emails.append(full_email)
        emails.append(full_email2)
        emails.append(full_email3)
        emails.append(full_email4)
        emails.append(full_email1)
        return random.choice(emails)
