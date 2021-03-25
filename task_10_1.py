class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        for el in range(len(self.matrix)):
            print('|', end=' ')
            for elem in range(len(self.matrix[el])):
                print(self.matrix[el][elem], end=' ')
            print('|')

    def __add__(self, other):
        if type(self.matrix[0]) != list:
            _ = self.matrix
            self.matrix = []
            self.matrix.append(_)
        if type(other.matrix[0]) != list:
            _ = other.matrix
            other.matrix = []
            other.matrix.append(_)
        if len(self.matrix) > len(other.matrix):
            for i in range(len(self.matrix) - len(other.matrix)):
                other.matrix.append([])
        if len(self.matrix) < len(other.matrix):
            for i in range(len(other.matrix) - len(self.matrix)):
                self.matrix.append([])
        for j in range(len(self.matrix)):
            for v in range(len(other.matrix)):
                if len(self.matrix[j]) > len(other.matrix[v]):
                    for i in range(len(self.matrix[j]) - len(other.matrix[v])):
                        other.matrix[v].append(0)
                if len(self.matrix[j]) < len(other.matrix[v]):
                    for i in range(len(other.matrix[v]) - len(self.matrix[j])):
                        self.matrix[j].append(0)
        list1 = [[0 for elem in range(len(self.matrix[el]))] for el in range(len(self.matrix))]
        for el in range(len(self.matrix)):
            for elem in range(len(self.matrix[el])):
                try:
                    int(self.matrix[el][elem])
                except ValueError:
                    self.matrix[el][elem] = 0
                try:
                    int(other.matrix[el][elem])
                except ValueError:
                    other.matrix[el][elem] = 0
                list1[el][elem] = (int(self.matrix[el][elem]) + int(other.matrix[el][elem]))
        return Matrix(list1)


matrix1 = Matrix([[88, 'h', 45, 6], ['4564', False, 45, 'k']])
matrix2 = Matrix([['str'], ['58', 32], [True, 33]])
try:
    print(matrix1 + matrix2)
except TypeError:
    ''
