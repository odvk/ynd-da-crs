#Переименование столбцов

#Задача3 / 4
#Переименуем столбцы таблицы, которая хранится в переменной df.
#Вызовите метод set_axis() и передайте ему список new_names, а значением аргумента inplace установите True.

import pandas as pd
df = pd.read_csv('music_log.csv')

new_names = ['user_id', 'total_play_seconds', 'artist_name', 'genre_name', 'track_name']

# ниже код
df.set_axis(new_names, axis = 'columns', inplace = True)
