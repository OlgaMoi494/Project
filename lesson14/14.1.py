class Alphabet:
    def __init__(self, end, lower=True):
        self.end = end
        self.lower = lower

    def __iter__(self):
        if self.lower:
            self.start_index = ord('a')
            self.end_index = ord(self.end)
        else:
            self.start_index = ord('A')
            self.end_index = ord(self.end.upper())

        return self

    def __next__(self):
        if self.start_index > self.end_index:
            raise StopIteration
        else:
            res = chr(self.start_index)
            self.start_index += 1
            return res
