#Обработка пропущенных значений
#Задача2 / 6
#Посчитайте количество пропущенных значений и выведите его на экран.

import pandas as pd
df = pd.read_csv('music_log_upd_col.csv')

print(df.isnull().sum())
