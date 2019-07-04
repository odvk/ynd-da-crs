#Получение данных
#Задача2 / 2
#Прочитайте файл music_log.csv и сохраните его в переменной df. Сохраните последние 10 строк с данными из music_log.csv в переменной music_tail и выведите значение переменной на экран.

# <импортируйте библиотеку pandas>
import pandas as pd
df = pd.read_csv('music_log.csv') # аргумент - путь к файлу

music_tail=df.tail(10)

print(music_tail)
