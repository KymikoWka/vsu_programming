num = []
b = input("Строка: ")
ch = int(input("Число: "))
for a in b:
    if "0" <= a <= "9":
        num.append(a)
print(num[ch - 1])