class EmptyStack(Exception):
    pass


class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if len(self._data) == 0:
            raise EmptyStack
        return self._data.pop()

    def peek(self):
        if len(self._data) == 0:
            return None
        return self._data[-1]

    @property
    def size(self):
        return len(self._data)
