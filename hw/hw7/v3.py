class Matrix:

    def __init__(self):
        self.string = None
        self.column = None
        self.matrix = []

    def rec(self):
        self.string = int(input("Введи количество строк: "))
        self.column = int(input("Введи количество столбцов: "))
        for a in range(self.column):
            self.matrix.append([int(input("Введи элемент матрицы: "))
                                for b in range(self.string)])

    def output(self):
        for x in self.matrix:
            print(' '.join([str(_) for _ in x]))


a = Matrix()
a.rec()
a.output()
