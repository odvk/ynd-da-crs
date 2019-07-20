#Группировка данных
#Задача1 / 3
#Меломаны у нас есть. Сейчас узнаем идентификатор user_id одного из них. Для этого сгруппируем данные по каждому пользователю, чтобы собрать жанры прослушанных им композиций.

#Сгруппируйте DataFrame по столбцу user_id, сохраните полученный результат в переменной genre_grouping (от англ. genre, «жанр» и grouping, «группировка»).

#Посчитайте количество жанров, которые выбрали пользователи, методом count(), указав, что выбираем один столбец genre_name. Сохраните результат в переменной genre_counting и выведите первые 30 строк этой таблицы.

import pandas as pd
df = pd.read_csv('music_log_upd.csv')

genre_grouping = df.groupby('user_id')
genre_counting = df.groupby('user_id')['genre_name'].count()
print(genre_counting.head(30))
