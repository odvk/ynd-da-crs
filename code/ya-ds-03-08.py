#8. Изменение списков в цикле

#Для начала давайте научимся изменять простые списки со значениями столбцов. Представим, что значения в некотором списке имеют типы int и float, а мы хотим преобразовать все значения к типу float. Очевидный способ — поменять переменную цикла — не сработает:

emojixpress = [
    2.26, 19.1, 25.6, 233, 15.2, 22.7, 64.6, 87.5, 6.81, 6,
    4.72, 24.7, 21.7, 10, 118, 3.31, 23.1, 1.74, 4.5, 0.0333
]

print('Список до изменения:')
print(emojixpress)
print()

for element in emojixpress:
    element = float(element)
    
print('Список после попытки изменения:')
print(emojixpress)

#Проблема — в самом устройстве цикла for. Он копирует элементы списка. Поэтому строка
element = float(element)
#меняет переменную element, но не меняет элемент списка.

# Вместо того, чтобы перебирать непосредственно элементы списка, мы можем перебирать их индексы — то есть просто числа от нуля до длины списка (не включая саму длину). Это делают вызовом функции range() (англ. range, «диапазон»). Ей передаётся какой-нибудь аргумент, например, 5, и она перебирает все числа от 0 до своего аргумента (не включая его): 0, 1, 2, 3, 4. Поместив результат в цикл for, можно распечатать эти числа:

for element in range(5):
    print(element)
	
# К сожалению, просто посмотреть результат выполнения функции range() не удастся:
range(5)
range(0, 5)

#Дело в том, что Python не хранит все числа от 0 до 5, а просто запоминает, от какого и до какого числа создаётся последовательность. Это особенно полезно для вызовов функции вроде range(1000000000).

#Опробуем новый принцип перебора элементов списка. У каждого элемента списка есть свой индекс. Чтобы пройтись по всем индексам списка emojixpress, используя функцию range(), передадим ей аргумент len(emojixpress):

emojixpress = [
    2.26, 19.1, 25.6, 233, 15.2, 22.7, 64.6, 87.5, 6.81, 6,
    4.72, 24.7, 21.7, 10, 118, 3.31, 23.1, 1.74, 4.5, 0.0333
]

for i in range(len(emojixpress)):
    print(emojixpress[i])

# Теперь мы можем поменять каждый элемент списка по очереди:

emojixpress = [
    2.26, 19.1, 25.6, 233, 15.2, 22.7, 64.6, 87.5, 6.81, 6,
    4.72, 24.7, 21.7, 10, 118, 3.31, 23.1, 1.74, 4.5, 0.0333
]

print('Список до изменения:')
print(emojixpress)
print()

for i in range(len(emojixpress)):
    emojixpress[i] = float(emojixpress[i])
    
print('Список после изменения:')
print(emojixpress)

