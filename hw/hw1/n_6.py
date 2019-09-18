print("Введите x и y ")
x = int(input('x '))
y = int(input("y "))
b = 0
for c in range(x, y + 1):
    if not c % 5:
        b += c
print(b)