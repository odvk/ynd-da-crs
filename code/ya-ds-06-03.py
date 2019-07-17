Охота на мусор
Задача
Просмотрите информацию о наборе данных: воспользуйтесь методом info().

import pandas as pd
df = pd.read_csv('music_log.csv')

df.info()


#Результат
#<class 'pandas.core.frame.DataFrame'>
#RangeIndex: 67963 entries, 0 to 67962
#Data columns (total 5 columns):
#  user_id     67963 non-null object
#total play    67963 non-null float64
#Artist        60157 non-null object
#genre         65223 non-null object
#track         65368 non-null object
#dtypes: float64(1), object(4)
#memory usage: 2.6+ MB