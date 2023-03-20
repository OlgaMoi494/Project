class Contact:
    def __init__(self, email, phone, first_name, last_name):
        self.email = email
        self.phone = phone
        self.first_name = first_name
        self.last_name = last_name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not isinstance(value, str):
            raise ValueError("email should be string.")
        if "@" not in value:
            raise ValueError("email should contain @ symbol.")
        if value.split("@")[1] not in ["gmail.com", "yandex.ru", "ya.ru",
                                       "yacho.com"]:
            raise ValueError(
                'email should end in list:\
                  "gmail.com", "yandex.ru", "ya.ru", "yacho.com".')

        self._email = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        if not value[0] == "+":
            raise ValueError("phone should start from +.")
        if int(value[1:4]) not in [375, 374] and int(value[1:3]) != 48:
            raise ValueError("Phone country code should be 375, 374 or 48.")

        self._phone = value

    def _name_validator(self, value):
        if not isinstance(value, str):
            raise ValueError("Name should be string.")
        if not value[0].isupper():
            raise ValueError("Name should start from capital letter.")
        if len(value) not in range(5, 16):
            raise ValueError("Name length should be in range (5, 15).")

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._name_validator(value)
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._name_validator(value)
        self._last_name = value
