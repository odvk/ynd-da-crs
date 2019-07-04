#Объект DataFrame
#Задача2 / 4
#Сколько наблюдений в наборе данных? В переменной shape_table хранится кортеж. Его первый элемент — количество наблюдений, который надо сохранить в переменной observations_table (не забывайте, что индексация элементов идет с 0). Напечатайте на экране ответ в таком виде:
#Количество наблюдений: ...

import pandas as pd
df = pd.read_csv('music_log.csv') 
shape_table = df.shape


# <напишите код здесь>
observations_table = shape_table[0]

print('Количество наблюдений: {}'.format(observations_table))