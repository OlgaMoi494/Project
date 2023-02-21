class EmptyLibraryError(Exception):
    ...


class Book:
    def __init__(self, name, description, pages, price):
        self.name = name
        self.description = description
        self.pages = pages
        self.price = price

    def to_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'pages': self.pages,
            'price': self.price
        }

    def contains_word(self, word):
        return word in self.name or word in self.description

    def __gt__(self, other):
        return self.pages > other.pages

    def __lt__(self, other):
        return self.pages < other.pages

    def __ge__(self, other):
        return self.pages >= other.pages

    def __le__(self, other):
        return self.pages <= other.pages

    def __eq__(self, other):
        return self.name == other.name and \
               self.description == other.description and \
               self.pages == other.pages and \
               self.price == other.price

    def __ne__(self, other):
        return self.name != other.name or \
               self.description != other.description or \
               self.pages != other.pages or \
               self.price != other.price


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: dict):
        return self.books.append(book)

    def get_books(self):
        return [book.to_dict() for book in self.books]

    def remove_book(self, book):
        self.books.remove(book)

    def find_the_biggest_book(self):
        try:
            if not self.books:
                raise EmptyLibraryError('No book in the library')
            else:
                max_pages = max(
                    [book.to_dict()['pages'] for book in self.books])
                book_max_pages = list(
                    filter(lambda x: x.to_dict()['pages'] == max_pages,
                           self.books))
                return book_max_pages[0].to_dict()
        except EmptyLibraryError as err:
            return err

    def __len__(self):
        return len(self.books)
