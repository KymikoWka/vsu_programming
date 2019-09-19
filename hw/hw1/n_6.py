print("Введите число ")
x = float(input('x: '))
if x == int(x) or not x % 1:
    print("Число не дробное")
else:
    print("Число дробное")