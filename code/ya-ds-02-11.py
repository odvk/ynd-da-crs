#Выравнивание текста
#Задача3 / 3
#Обновите код вывода всей таблицы, добавив выравнивание и вывод чисел с точностью до двух знаков после запятой. Результат должен выглядеть так:
#Название эмодзи  | EmojiXpress, млн | Instagram, млн | Твиттер, млн
#-------------------------------------------------------------------
#Ухмыляюсь        |             2.26 |           1.02 |        87.30
#Сияю от радости  |            19.10 |           1.69 |       150.00
#Катаюсь от смеха |            25.60 |           0.77 |         0.00   
#...

data = [
    ['Ухмыляюсь', 2.26, 1.02, 87.3],
    ['Сияю от радости', 19.1, 1.69, 150.0],
    ['Катаюсь от смеха', 25.6, 0.774, 0.0],
    ['Слёзы радости', 233.0, 7.31, 2270.0],
    ['Подмигиваю', 15.2, 2.36, 264.0],
    ['Счастлив', 22.7, 4.26, 565.0],
    ['Глаза-сердца', 64.6, 11.2, 834.0],
    ['Целую', 87.5, 5.13, 432.0],
    ['Задумчивость', 6.81, 0.636, 0.0],
    ['Равнодушие', 6.0, 0.236, 478.0],
    ['Солнечные очки', 4.72, 3.93, 198.0],
    ['Громко плачу', 24.7, 1.35, 654.0],
    ['След от поцелуя', 21.7, 2.87, 98.7],
    ['Два сердца', 10.0, 5.69, 445.0],
    ['Сердце', 118.0, 26.0, 1080.0],
    ['Червы', 3.31, 1.82, 697.0],
    ['Класс', 23.1, 3.75, 227.0],
    ['Пожимаю плечами', 1.74, 0.11, 0.0],
    ['Огонь', 4.5, 2.49, 150.0],
    ['Переработка', 0.0333, 0.056, 932.0]
]


print('Название эмодзи  | EmojiXpress, млн | Instagram, млн | Твиттер, млн')
print('-------------------------------------------------------------------')
for row in data:
    # В функцию format() можно передавать несколько
    # аргументов и для каждого указывать, как его выводить.
    # Напишите код форматирования вместо многоточий.
    print('{: <16} | {: >16.2f} | {: >14.2f} | {: >12.2f}'.format(row[0], row[1], row[2], row[3]))