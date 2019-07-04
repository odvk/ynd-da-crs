# 3. Библиотека Pandas

atlas = [
    ['Франция','Париж'],
    ['Россия','Москва'],
    ['Китай','Пекин'],
    ['Мексика','Мехико'],
    ['Египет','Каир'],
]
geography = ['country', 'capital']
world_map = pd.DataFrame(data = atlas , columns = geography) # таблица сохраняется в переменной с произвольно выбранным именем world_map
print(world_map) # вывод на экран