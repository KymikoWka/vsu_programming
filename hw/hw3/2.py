def get_season(n):
    seasons = {
        2 < n < 6: 'Весна',
        5 < n < 9: 'Лето',
        8 < n < 12: 'Осень',
        n == 12 or n < 3: 'Зима',
    }
    return seasons[True]


month = int(input('Месяц: '))
print(get_season(month))
