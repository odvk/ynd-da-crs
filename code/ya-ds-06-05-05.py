#Обработка пропущенных значений
#Задача5 / 6
#Удалите пропущенные значения из столбца 'genre_name'.

import pandas as pd
df = pd.read_csv('music_log_upd_col.csv')

df['track_name'] = df['track_name'].fillna('unknown')
df['artist_name'] = df['artist_name'].fillna('unknown')

df.dropna(subset = ['genre_name'], inplace = True)
