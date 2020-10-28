class Array:
    def __init__(self, *args):
        self._array = [*args]
    
    def __len__(self):
        return len(self._array)

    def push(self, item):
        self._array.append(item)

    def __repr__(self):
        return f'{self._array}'

    def __getitem__(self, key):
        return self._array[key]

    @staticmethod
    def fill(value, mul):
        return [value for _ in range(1, mul)]


if __name__ == '__main__':
    pass