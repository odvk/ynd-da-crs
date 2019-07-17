#Обработка пропущенных значений
#Задача6 / 6
#Проверьте полученный результат. Просмотрите информацию о наборе данных: воспользуйтесь методом info().

import pandas as pd
df = pd.read_csv('music_log_upd_col.csv')

df['track_name'] = df['track_name'].fillna('unknown')
df['artist_name'] = df['artist_name'].fillna('unknown')

df.dropna(subset = ['genre_name'], inplace = True)

df.info()
