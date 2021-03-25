class Cell:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        self.value += other.value
        del other
        return self.value

    def __sub__(self, other):
        if self.value - other.value > 0:
            self.value -= other.value
            del other
            return self.value
        else:
            return 'Вторая клетка содержит больше ячеек, чем первая'

    def __mul__(self, other):
        self.value *= other.value
        del other
        return self.value

    def __floordiv__(self, other):
        self.value //= other.value
        del other
        return self.value

    def make_order(self, str_value):
        end_str = ''
        mod = self.value % str_value
        i = 0
        while i < (self.value - mod):
            for j in range(str_value):
                end_str += '*'
                i += 1
            end_str += '\n'
        for i in range(mod):
            end_str += '*'
        return end_str


example1 = Cell(21)
example2 = Cell(14)
print(example1.make_order(18))
