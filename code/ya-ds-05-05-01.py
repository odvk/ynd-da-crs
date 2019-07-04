#Объект DataFrame
#Задача1 / 4
#Прочитайте файл music_log.csv и сохраните его в переменной df. Создайте переменную shape_table и сохраните в ней размеры таблицы music_log.csv. Напечатайте на экране размер таблицы в таком виде:
#Размер таблицы: ...

import pandas as pd

df = pd.read_csv('music_log.csv') # аргумент - путь к файлу
shape_table=df.shape 
print('Размер таблицы: {}'.format(shape_table))