#Описательная статистика
#Задача2 / 7
#Найдите максимальное время прослушивания песни в жанре pop. Сохраните результат в переменной pop_music_max_total_play и выведите её значение на экран.

import pandas as pd
df = pd.read_csv('music_log_upd.csv')

pop_music = df [(df['genre_name'] == 'pop') & (df['total_play_seconds'] != 0)]
#print(pop_music.head(20))
#print()

# код ниже
pop_music_max_total_play = pop_music['total_play_seconds'].max()
#pop_music_max_total_play = df [(df['genre_name'] == 'pop')]['total_play_seconds'].max()
print(pop_music_max_total_play)

