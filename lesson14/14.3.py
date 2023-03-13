class IncorrectDataError(Exception):
    ...


class Element:
    def __init__(self, data: int):
        self.data = data
        self.next = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, set_data):
        if set_data not in range(0, 10001):
            raise IncorrectDataError("Data should be in range from 0 to 10000")
        self._data = set_data

    def __eq__(self, other):
        return self.data == other.data

    def __gt__(self, other):
        return self.data > other.data

    def __ge__(self, other):
        return self.data >= other.data


class LinkedList:

    def __init__(self, head=None):
        self.head = head
        self.length = 0
        self.lst = []

    def append(self, element):
        new_element = Element(element)
        if not self.head:
            self.head = new_element
            self.length += 1
            self.lst.append(new_element)
            return
        current_element = self.head
        while current_element.next:
            current_element = current_element.next
        current_element.next = new_element
        self.length += 1
        self.lst.append(new_element)

    def reverse(self):
        if not self.head:
            return
        current_element = self.head
        new_next = None
        while current_element:
            temporary = current_element.next
            current_element.next = new_next
            new_next = current_element
            current_element = temporary
        self.head = new_next
        self.lst = self.lst[::-1]

    def __iter__(self):
        self.current_element = self.head
        return self

    def __next__(self):
        if not self.current_element:
            raise StopIteration
        else:
            res = self.current_element.data
            self.current_element = self.current_element.next
            return res

    def __len__(self):
        return self.length

    def println(self):
        print([element.data for element in self.lst])
