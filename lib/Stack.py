class Stack:
    def __init__(self, items=None, limit=100):
        self._stack = items if items is not None else []
        self.limit = limit

    @property
    def items(self):
        return self._stack

    def isEmpty(self):
        return self.empty()

    def empty(self):
        return len(self._stack) == 0

    def push(self, item):
        if self.limit is not None and len(self._stack) >= self.limit:
            return
        self._stack.append(item)

    def pop(self):
        if self.empty():
            return None
        return self._stack.pop()


    def peek(self):
        if self.empty():
            return None
        return self._stack[-1]

    def size(self):
        return len(self._stack)

    def full(self):
        if self.limit is None:
            return False
        return len(self._stack) == self.limit

    def search(self, target):
        try:
            index_from_top = self._stack[::-1].index(target)
            return index_from_top
        except ValueError:
            return -1
