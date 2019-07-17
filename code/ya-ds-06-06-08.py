#Обработка дубликатов
#Задача8 / 8
#Оцените изменения: пересчитайте количество значений 'электроника' в столбце 'genre_name'. Если удалось всё заменить, результат должен быть равен 0. Сохраните этот результат в переменной genre_final_count (от англ. final count, «окончательный подсчёт»), выведите на экран.

import pandas as pd
df = pd.read_csv('music_log_upd_nan.csv')

df['genre_name'] = df['genre_name'].replace('электроника', 'electronic')

genre_final_count = df[df['genre_name'] == 'электроника']['genre_name'].count()
print(genre_final_count)
