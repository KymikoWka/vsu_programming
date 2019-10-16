lst = []
a = input("Введите элементы: ")
while a:
    lst.append(a)
    a = input()
for i in set(lst):
    print(i, "|", lst.count(i))
