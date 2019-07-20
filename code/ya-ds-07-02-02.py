#С чего начинается исследование
#Задача2 / 4
#Получите список названий столбцов, запросив атрибут columns. Результат выведите на экран.

import pandas as pd
df = pd.read_csv('music_log_upd.csv')

print(df.columns)