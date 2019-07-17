#Обработка дубликатов
#Задача1 / 8
#Сохраните текущий размер таблицы в переменной shape_table.

import pandas as pd
df = pd.read_csv('music_log_upd_nan.csv')

shape_table = df.shape
print(df.shape)