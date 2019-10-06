num = []
b = input("Строка: ")
ch = int(input("Число: "))
for a in b:
    if "9" >= a >= "0":
        num.append(a)
print(num[ch - 1])