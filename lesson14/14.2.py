class Stack:
    def __init__(self):
        self.stack_list = []

    def push(self, element):
        return self.stack_list.append(element)

    def pop(self):
        if not self.stack_list:
            return None
        return self.stack_list.pop()

    def is_empty(self):
        if not self.stack_list:
            return True
        return False

    def peek(self):
        if not self.stack_list:
            return None
        return self.stack_list[-1]


def check_brackets(string):
    stack_open = Stack()
    for symbol in string:
        if symbol in "{[(":
            stack_open.push(symbol)
        elif symbol in "]})":
            if stack_open.is_empty():
                return False
            else:
                if symbol == ")" and stack_open.peek() == "(" or \
                        symbol == "]" and stack_open.peek() == "[" or \
                        symbol == "}" and stack_open.peek() == "{":
                    stack_open.pop()
    return True
