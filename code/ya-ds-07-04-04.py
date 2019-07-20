#Сортировка данных
#Задача4 / 5
#Чтобы предпочтения были видны сразу, нужно крупнейшие значения расположить наверху. Отсортируйте данные в группировке sum_music_user по убыванию. Внимание: когда применяете метод sort_values() к Series с единственным столбцом, аргумент by указывать не нужно, только порядок сортировки.
#Сохраните результат в переменной final_sum и выведите её значение на экран.
#Команду «распечатать сумму» из прошлой задачи закомментируйте.

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

# код ниже
final_sum = sum_music_user.sort_values(ascending = False)
print(final_sum)