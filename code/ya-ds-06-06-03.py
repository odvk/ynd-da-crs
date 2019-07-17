#Обработка дубликатов
#Задача3 / 8
#Удалите дубликаты. Используйте метод reset_index() для сохранения порядка индексов.

import pandas as pd
df = pd.read_csv('music_log_upd_nan.csv')

shape_table = df.shape

df = df.drop_duplicates().reset_index(drop=True)