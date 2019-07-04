#Объект DataFrame
#Задача3 / 4
#Найдите в информации, которую вернул метод info(), число наблюдений. Вручную присвойте это число как значение переменной observations_info_table.

import pandas as pd
df = pd.read_csv('music_log.csv')
#  <вот здесь напишите вызов метода info() и нажмите кнопку "Выполнить">
# <observations_info_table =   а затем раскомментируйте и впишите полученное количество наблюдений сюда>

print(df.info())
observations_info_table = 67963 