#Описательная статистика
#Задача3 / 7
#Получите строку таблицы pop_music c информацией о самой длинной по времени прослушивания песне жанра 'pop' и сохраните её в переменной pop_music_max_info. Выведите эту строку на экран. Закомментируйте вывод результата предыдущей задачи.

import pandas as pd
df = pd.read_csv('music_log_upd.csv')

# код ниже
pop_music = df [(df['genre_name'] == 'pop') & (df['total_play_seconds'] != 0)]
#print(pop_music.head(20))
#print()

pop_music_max_total_play = pop_music['total_play_seconds'].max()
#pop_music_max_total_play = df [(df['genre_name'] == 'pop')]['total_play_seconds'].max()
#print(pop_music_max_total_play)

#код ниже 
pop_music_max_info = pop_music[pop_music['total_play_seconds'] == pop_music_max_total_play]
print(pop_music_max_info)
