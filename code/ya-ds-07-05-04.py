#Описательная статистика
#Задача4 / 7
#Найдите минимальное ненулевое время прослушивания композиции в жанре pop. Сохраните его в переменной pop_music_min_total_play, значение выведите на экран. Вывод результата предыдущей задачи закомментируйте.

import pandas as pd
df = pd.read_csv('music_log_upd.csv')

# код ниже
pop_music = df [(df['genre_name'] == 'pop') & (df['total_play_seconds'] != 0)]
#print(pop_music.head(20))
#print()

pop_music_max_total_play = pop_music['total_play_seconds'].max()
#pop_music_max_total_play = df [(df['genre_name'] == 'pop')]['total_play_seconds'].max()
#print(pop_music_max_total_play)
pop_music_max_info = pop_music[pop_music['total_play_seconds'] == pop_music_max_total_play]
#print(pop_music_max_info)

# код здесь
pop_music_min_total_play = pop_music['total_play_seconds'].min()
print(pop_music_min_total_play)
