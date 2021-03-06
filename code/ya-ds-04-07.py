#7. Условный оператор
#Мы хотели увидеть, как меняются вкусы Киноакадемии. Для такого анализа нужно научить Python различать новые и старые фильмы.
#Тут на помощь приходит условный оператор. Он позволяет создавать «развилки»: то есть задавать условие и выполнять один код, если оно выполняется, и другой — в противном случае.
#Напишем функцию для проверки, получил ли фильм «Оскар» в течение последних 10 лет:

# функция
def check_if_recent(year):
    if year < 2008:
        print('Фильм был снят давно')
    else:
        print('Фильм свежий')

# примеры использования
print('Бёрдмэн')
check_if_recent(2014)
print('Титаник')
check_if_recent(1997)

# Ключевые слова if (англ. if, «если») и else (англ. else, «иначе») задают условный оператор. Если условие выполнено, Python исполнит один код, а если нет — другой. На схеме изображён синтаксис условного оператора:
# схема в файле
