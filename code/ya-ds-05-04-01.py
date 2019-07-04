#Получение данных
#Задача1 / 2
#Прочитайте файл music_log.csv и сохраните его в переменной df. Сохраните первые 5 строк с данными из music_log.csv в переменной music_head и выведите значение переменной на экран.

# <импортируйте библиотеку pandas>
import pandas as pd

df = pd.read_csv('music_log.csv') # аргумент - путь к файлу

music_head = df.head()

print(music_head)

