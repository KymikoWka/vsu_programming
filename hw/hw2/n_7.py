from random import randint
rand = randint(0, 100)
a = int(input("Ввод: "))
while a != rand:
    if a > rand:
        print("Загаданное число меньше")
    else:
        print("Загаданное число больше")
    a = int(input("Ввод: "))
print("Вы угадали число")