#Сортировка данных
#Задача5 / 5
#Теперь то же самое надо сделать с числом прослушанных меломаном композиций. Отсортируйте данные группировки count_music_user по убыванию. Сохраните результат в переменной final_count, значение которой выведите на экран.
#Команду «распечатать» из прошлой задачи закомментируйте.

import pandas as pd
df = pd.read_csv('music_log_upd.csv')

genre_grouping = df.groupby('user_id')['genre_name']

def user_genres(group):
    for col in group:
        if len(col[1]) > 50:
            user = col[0]
            return user

search_id = user_genres(genre_grouping)

music_user = df[(df['user_id'] == search_id) & (df['total_play_seconds']>0)]
#print(music_user.head())

sum_music_user = music_user.groupby('genre_name')['total_play_seconds'].sum()
#print(sum_music_user)
#print()
count_music_user = music_user.groupby('genre_name')['genre_name'].count()
#print(count_music_user)

final_sum = sum_music_user.sort_values(ascending = False)
#print(final_sum)
#print()

# код ниже
final_count = count_music_user.sort_values(ascending = False)
print(final_count)
print()

