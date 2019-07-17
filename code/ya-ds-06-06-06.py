#Обработка дубликатов
#Задача6 / 8
#Получите уникальные значения столбца 'genre_name', используйте метод unique(). Просмотрите результат и найдите название жанра, которое выпадает из общего ряда.

import pandas as pd
df = pd.read_csv('music_log_upd_nan.csv')

print(df['genre_name'].unique())
