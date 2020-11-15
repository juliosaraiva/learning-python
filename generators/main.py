class Generator:
    current = 0

    def __init__(self, end, start=0):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if Generator.current < self.end:
            num = Generator.current
            Generator.current += 1
            return num
        raise StopIteration


gen = Generator(50)
for item in gen:
    print(item)
