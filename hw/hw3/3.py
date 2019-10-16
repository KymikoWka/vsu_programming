n = int(input("Введите номер последовательности Фибоначчи: "))
a = [0, 1]
for i in range(n - 2):
    a.append(a[-1] + a[-2])
print(a)
