#Индексация в DataFrame
#Задача3 / 4
#Теперь посчитайте число прослушанных треков в жанре рок. Допишите в код подсчёт, похожий на предыдущий, только с логическим условием df['genre'] == 'rock'. Сохраните результат в переменной genre_rock. Напечатайте ответ на экране в таком виде:
#Число прослушанных треков в жанре рок равно ...

import pandas as pd
df = pd.read_csv('music_log.csv')

genre_fight=df.loc[:,['genre', 'Artist']]

genre_pop = genre_fight.loc[genre_fight.loc[:,'genre'] == 'pop']['genre'].count()
print('Число прослушанных треков в жанре поп равно', genre_pop)

genre_rock = genre_fight.loc[genre_fight.loc[:,'genre'] == 'rock']['genre'].count()
print('Число прослушанных треков в жанре рок равно', genre_rock)

