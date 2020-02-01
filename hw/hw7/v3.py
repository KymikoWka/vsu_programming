class Matrix:

    def __init__(self):
        self.strng = None
        self.column = None
        self.mtrx = []

    def rec(self):
        self.strng = int(input("Введи количество строк: "))
        self.column = int(input("Введи количество столбцов: "))
        self.mtrx.append([[input("Введи элемент матрицы: ")
                           for a in range(self.column)] for b in range(self.strng)])

    def output(self):
        for row in self.mtrx:
            for mtrx in row:
                print(mtrx, end=' ')
                print()


a = Matrix()
a.rec()
a.output()
