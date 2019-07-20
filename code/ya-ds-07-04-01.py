#Сортировка данных
#Задача1 / 5
#Космический телескоп Kepler открыл похожую на Землю планету у похожей на Солнце звезды. А вы в данных Яндекс.Музыки обнаружили меломана с уникальными данными. Он за день послушал больше 50 композиций.
#Получите таблицу с прослушанными им треками.
#Для этого запросите из структуры данных df строки, отвечающие сразу двум условиям:
#1) значение в столбце 'user_id' должно быть равно значению переменной search_id;
#2) время прослушивания, т.е. значение в столбце 'total_play_seconds', не должно равняться 0.
#Сохраните результат в переменной music_user.

import pandas as pd
df = pd.read_csv('music_log_upd.csv')

genre_grouping = df.groupby('user_id')['genre_name']

def user_genres(group):
    for col in group:
        if len(col[1]) > 50:
            user = col[0]
            return user

search_id = user_genres(genre_grouping)

#код ниже

music_user = df[(df['user_id'] == search_id) & (df['total_play_seconds']>0)]
print(music_user)

