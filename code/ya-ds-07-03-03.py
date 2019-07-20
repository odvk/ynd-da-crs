#Группировка данных
#Задача3 / 3
#Вызовите функцию user_genres, как аргумент передайте ей genre_grouping. Результат – user_id неведомого нам любителя музыки – сохраните в переменной search_id (от англ. search id, «искать идентификатор») и выведите значение на экран.

import pandas as pd
df = pd.read_csv('music_log_upd.csv')

genre_grouping = df.groupby('user_id')['genre_name']


def user_genres(group):
    for col in group:
        if len(col[1]) > 50:
            user = col[0]
            return user


# код ниже
			
search_id = user_genres(genre_grouping)
print(search_id)
