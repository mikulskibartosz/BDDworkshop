class LRU:
    def __init__(self, max_size=1):
        self.list = []
        self.max_size = max_size

    def __len__(self):
        return len(self.list)

    def __add__(self, other):
        self.list.append(other)

        if len(self.list) > self.max_size:
            self.list.pop(0)

        return self

    def __str__(self):
        return str(self.list)

    def __iter__(self):
        yield from self.list
