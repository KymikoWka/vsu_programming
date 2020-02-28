class Matrix:
    def __init__(self, mat=[]):
        self.string = None
        self.column = None
        self.mat = mat

    def input_mat(self):
        self.string = int(input('Строки: '))
        self.column = int(input('Столбцы: '))
        self.mat = [[int(input('Элементы: ')) for x in range(self.column)]
                    for x in range(self.string)]

    def __str__(self):
        return '\n'.join(' '.join(str(i) for i in x) for x in self.mat)

    def set_element(self, s, c, value):
        self.__check_value(value)
        self.mat[s][c] = value

    def __check_value(self, value):
        if not isinstance(value, int):
            raise ValueError("Значение должно быть числом!")


class Matrix2x2(Matrix):
    def __init__(self, mat):
        if list(map(len, mat)).count(2) != 2:
            raise ValueError("Матрица должна быть 2х2")
        super().__init__(mat)

    def determinant(self):
        print(self.mat[0][0] * self.mat[1][1] -
              self.mat[0][1] * self.mat[1][0])


m = Matrix()
m.input_mat()
x = 9
m.set_element(1, 1, x)
print(m)
