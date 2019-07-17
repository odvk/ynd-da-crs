#Индексация в DataFrame
#Задача1 / 4
#Получите таблицу, состоящую из столбцов genre и Artist. Сохраните её в переменной genre_fight.

import pandas as pd
df = pd.read_csv('music_log.csv')

#print(df.info())

genre_fight=df.loc[:,['genre', 'Artist']]
