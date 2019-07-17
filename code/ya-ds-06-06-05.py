#Обработка дубликатов
#Задача5 / 8
#Сравните переменные shape_table и shape_table_update. Если они равны, выведите сообщение 'Размер таблицы не изменился, текущий размер:' и значение переменной shape_table_update.
#В ином случае сообщение должно быть таким: 'Таблица уменьшилась, текущий размер:'.

import pandas as pd
df = pd.read_csv('music_log_upd_nan.csv')

shape_table = df.shape

df = df.drop_duplicates().reset_index(drop=True)

shape_table_update = df.shape

if shape_table == shape_table_update:
    print('Размер таблицы не изменился, текущий размер:', shape_table_update)
else:
    print('Таблица уменьшилась, текущий размер:', shape_table_update)
