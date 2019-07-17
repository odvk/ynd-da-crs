#Обработка дубликатов
#Задача7 / 8
#В столбце 'genre_name' замените значение 'электроника' на 'electronic' .

import pandas as pd
df = pd.read_csv('music_log_upd_nan.csv')

df['genre_name'] = df['genre_name'].replace('электроника', 'electronic')