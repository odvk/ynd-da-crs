#Описательная статистика
#Задача1 / 7
#Получите таблицу с композициями самого популярного жанра — pop, исключив пропущенные треки. Сохраните результат в переменной pop_music.

import pandas as pd
df = pd.read_csv('music_log_upd.csv')

# код ниже
pop_music = df [(df['genre_name'] == 'pop') & (df['total_play_seconds'] != 0)]
#print(pop_music.head(30))