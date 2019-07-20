#Сортировка данных
#Задача2 / 5
#Теперь узнаем, сколько времени он слушал музыку каждого жанра.
#Сгруппируйте данные таблицы music_user по столбцу 'genre_name' и получите сумму значений столбца 'total_play_seconds'. #Сохраните результат в переменной sum_music_user и выведите её значение на экран.

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

# код ниже
sum_music_user = music_user.groupby('genre_name')['total_play_seconds'].sum()
print(sum_music_user)