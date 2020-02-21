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


class Matrix2x2(Matrix):
    def __init__(self, mat):
        if list(map(len, mat)).count(2) != 2:
            raise ValueError("Матрица должна быть 2х2")
        super().__init__(mat)

    def determinant(self):
        print(self.mat[0][0] * self.mat[1][1] -
              self.mat[0][1] * self.mat[1][0])


test = [[1, 2], [4, 5]]
det = Matrix2x2(test)
det.determinant()
