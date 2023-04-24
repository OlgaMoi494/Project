from time import time


class Censored:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        index_censored = value.lower().find("fuck")
        if index_censored >= 0:
            value = value[:index_censored] + "****" + value[index_censored+4:]
        setattr(instance, self.name, value)


class Message:
    text = Censored()

    def __init__(self, text):
        self.text = text
        self.created_at = time()


class Song:
    name = Censored()

    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.created_at = time()
