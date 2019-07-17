#Переименование столбцов

#Задача2 / 4
#Подготовьте список new_names (англ. new names, "новые имена") с новыми именами для столбцов.
#user_id > user_id
#total play > total_play_seconds
#Artist > artist_name
#genre > genre_name
#track > track_name


import pandas as pd
df = pd.read_csv('music_log.csv')

new_names = ['user_id', 'total_play_seconds', 'artist_name', 'genre_name', 'track_name']