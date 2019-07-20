#С чего начинается исследование
#Задача3 / 4
#Посчитайте количество пустых значений в наборе данных, сохраните результат в переменной na_number. (от англ. no answer number, «количество плейсхолдеров “нет ответа”»). Выведите её значение на экран.

import pandas as pd
df = pd.read_csv('music_log_upd.csv')

na_number = df.isna().sum()
print(na_number)

