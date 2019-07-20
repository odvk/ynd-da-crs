#С чего начинается исследование
#Задача4 / 4
#Посчитайте количество дубликатов в наборе данных, сохраните результат в переменной duplicated_number (от англ. duplicated number, «число дубликатов»). Выведите её значение на экран.

import pandas as pd
df = pd.read_csv('music_log_upd.csv')

duplicated_number = df.duplicated().sum()
print(duplicated_number)