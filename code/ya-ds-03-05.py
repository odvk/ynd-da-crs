#5. Сортировка по столбцу

#Напомним, что Python хранит таблицу как список списков. Если нужно отсортировать её по определенному столбцу, его указывают именованным аргументом key (англ. key, «ключ»).

#Python не считает наш список из списков таблицей. Он видит только перечень строк. Столбцов в этой таблице для Python не существует. Чтобы отсортировать таблицу по столбцу с индексом 1, нам нужно пояснить: считай, что последовательность для сортировки состоит из элементов каждой строки с индексом 1, и по этой последовательности сортируй. Это объяснение делается лямбда-функцией — короткой безымянной функцией:

# lambda row: row[1]

# Эта функция принимает на вход очередную строку row и возвращает столбец из элементов каждой строки с индексом 1. В нашем случае это записывается row[1]. Название row для очередных строк мы выбрали сами для наглядности, можете придумать и другое. Создавать полноценные собственные функции вы научитесь в следующей теме, а пока для сортировки годится простенькая лямбда-функция.

# Переставим строки таблицы так, чтобы элементы столбца «EmojiXpress, млн» расположились в порядке возрастания:
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

data.sort(key=lambda row: row[1])

print('Название эмодзи  | EmojiXpress, млн |', end='')
print(' Instagram, млн | Твиттер, млн')
print('-------------------------------------', end='')
print('------------------------------')
for row in data:
    print('{: <16} | {: >16.2f} | {: >14.2f} | {: >12.2f}'.format(
        row[0], row[1], row[2], row[3]))
		
		
# Именованные аргументы можно комбинировать. Например, давайте отсортируем данные столбца «EmojiXpress, млн» по убыванию, применяя одновременно key и reverse:

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

data.sort(key=lambda row: row[1], reverse=True)

print('Название эмодзи  | EmojiXpress, млн |', end='')
print(' Instagram, млн | Твиттер, млн')
print('-------------------------------------', end='')
print('------------------------------')
for row in data:
    print('{: <16} | {: >16.2f} | {: >14.2f} | {: >12.2f}'.format(
        row[0], row[1], row[2], row[3]))

