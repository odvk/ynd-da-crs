#Переименование столбцов
#Задача1 / 4
#Выведите список столбцов.

import pandas as pd
df = pd.read_csv('music_log.csv')

#ниже код
print(df.columns)
