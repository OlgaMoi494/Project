import providers


class FakeFactory:
    def __init__(self, provider, number):
        self.provider = provider()
        self.number = number

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        if not isinstance(value, int):
            raise ValueError("Number should be whole number.")

        if value <= 0:
            raise ValueError("Number should be positive.")

        self._number = value

    def generate(self):
        return self.provider()

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index == self._number:
            raise StopIteration
        else:
            res = self.generate()
        self.index += 1
        return res


c1 = FakeFactory(providers.NameProvider, 10)
print(c1.generate())
