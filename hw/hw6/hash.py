# Это список из списков который будет длиной из 3 элементов
# Он нужен для хранения ключа и его значения
hash_table = [[] for _ in range(3)]


# Это функция которая возвращает хеш от ключа.
def hash_func(hash_str):
    hash_str = sum([ord(x) for x in hash_str]) % 3
    return hash_str


# Это функция которая добавляет пару ключ значение в список или обновляет её.
def set_value(key, value):
    # В пременнную записываем спиcок с парами.
    el = hash_table[hash_func(key)]
    # Итерируемся по парам.
    for pair in el:
        # Проверяем совпадают ли ключи у выбранной пары.
        if key == pair[0]:
            # Если совпадают, то перезаписываем значение у пары.
            pair[1] = value
            break
    # else выполнится, если цикл вышел не через break.
    else:
        # Добавляем новую пару в список.
        el.append([key, value])


# Функция которая возвращает значение ключа, которое введёт пользователь.
def get_value(key):
    # Цикл которай итерируется по парам(но мы сразу развернули значение и ключ)
    for k, v in hash_table[hash_func(key)]:
        # Проверяем ключи.
        if key == k:
            # Возвращаем значение.
            return v


# Цикл удаления ключа.
def del_pair(key):
    el = hash_table[hash_func(key)]
    for pair in el:
        if key == pair[0]:
            el.remove(pair)
            return True
    return False


set_value("abc", 1)
set_value("zxc", 2)
set_value("fd", 3)
set_value("a", 4)
set_value("d", 5)
set_value("2134", 6)
set_value("142155", 7)

set_value("abc", 999999999999)
print(get_value("abc"))
print(get_value("zxc"))
print(get_value("fd"))
print(get_value("a"))
print(get_value("d"))
print(get_value("2134"))
print(get_value("142155"))
print(get_value("142155e"))

print(del_pair("abc"))
