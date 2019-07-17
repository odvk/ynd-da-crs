#Индексация в DataFrame
#Задача4 / 4
#Напишите условную конструкцию, которая сравнивает полученные значения и выводит информацию о победителе в этом бою! Если победил жанр рок, то выведите сообщение "Рок победил!", а если победил жанр поп - сообщение "Попса forever!"

import pandas as pd
df = pd.read_csv('music_log.csv')

genre_fight=df.loc[:,['genre', 'Artist']]

genre_pop = genre_fight.loc[genre_fight.loc[:,'genre'] == 'pop']['genre'].count()
print('Число прослушанных треков в жанре поп равно', genre_pop)

genre_rock = genre_fight.loc[genre_fight.loc[:,'genre'] == 'rock']['genre'].count()
print('Число прослушанных треков в жанре рок равно', genre_rock)

if genre_rock >= genre_pop:
    print("Рок победил!")
else:
    print("Попса forever!")
