x = input("Введите x")
y = input("Введите y")
x = int(x)
y = int(y)
if x > 0 and y > 0:
    print("1 четверть")
elif x < 0 and y > 0:
    print("2 четверть")
elif x < 0 and y < 0:
    print ("3 четверть")
elif x > 0 and y < 0:
    print ("4 четверть")
else:
    print("На оси")