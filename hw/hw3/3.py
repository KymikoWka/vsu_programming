def print_feb_nums(n):
    feb = [0, 1]
    for i in range(n - 2):
        feb.append(feb[-1] + feb[-2])
    print(feb)


num = int(input("num: "))
print_feb_nums(num)
