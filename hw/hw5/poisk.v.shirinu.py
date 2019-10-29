from collections import deque


def players(s):
    return not len(s) % 2 and s[0] == "D"  # len - длина


names = {
    "Dima": ["Alice", "Paul"],
    "Alice": ["Carl", "Denis", "Edward"],
    "Paul": ["Denis", "Elise", "Nikita", "Alice", "Dona"],
}

d = deque(names["Dima"])  # Очередь
x = []
while names:
    doter = d.popleft()  # Удаляет и возвращает первый элемент очереди
    if doter not in x:  # Чтоб не повторялись друзья
        if players(doter):  # Еcли ТРУ то печатаю и выхожу из цикла
            print(doter)
            break  # Выход из while
        # В очередь докидываем друзей текущего человека, get - получение значения по ключу Doter
        d += names.get(doter, [])
        x.append(doter)  # Добавление в список тех, кого проверили
