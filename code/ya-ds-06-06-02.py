#Обработка дубликатов
#Задача2 / 8
#Посчитайте и выведите на экран суммарное количество дубликатов в таблице.

import pandas as pd
df = pd.read_csv('music_log_upd_nan.csv')

shape_table = df.shape
#print(shape_table)
print()
print(df.duplicated().sum())