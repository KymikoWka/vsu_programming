from collections import deque


def players(s):
    return not len(s) % 2 and s[0] == "D"


names = {
    "Dima": ["Alice", "Paul"],
    "ALice": ["Carl", "Denis", "Edward"],
    "Paul": ["Denis", "Elise", "Nikita", "Alice", "Dona"],
}

d = deque(names["Dima"])
x = []
while names:
    doter = d.popleft()
    if doter not in x:
        if players(doter):
            print(doter)
            break
        else:
            d += names.get(doter, [])
        x.append(doter)
