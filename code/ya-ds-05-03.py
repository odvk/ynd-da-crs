3. Библиотека Pandas
Вот так выглядят наши данные на этапе знакомства:
---файл 05-03-01-пример данных яндекс-музыка---


Этот хаос нужно превратить в аккуратную табличку, поддающуюся обработке. Для такой задачи подойдёт и Excel, но лучше использовать профильный инструмент — программную библиотеку Pandas.

Библиотеки – это наборы готовых методов для решения распространенных задач. Из того, что есть в Python, для операций с таблицами чаще всего применяют Pandas. Название — от сокращения panel data (англ. «панельные данные») — пришло из терминологии применяемого в экономике панельного анализа, который изучает изменение определенного признака у определённого объекта во времени (например, уровень бедности в Бразилии во второй половине 20 века). Библиотека Pandas оказалась таким универсальным инструментом, что годится для исследования любых данных, которые вообще можно собрать в таблицу.

Почему библиотека Pandas такая крутая и популярная? У неё богатейшие возможности:
* Готовые методы для всяческих манипуляций с таблицами: добавления, удаления, преобразования, агрегирования данных;
* Одновременная обработка данных из разных файлов;
* Готовые методы для операций с пропущенными значениями, выявления и устранения проблемных данных;
* Использование данных в самых разных форматах.

Инструменты библиотеки становятся доступны, когда мы вызываем её командой import (англ. import, «импортировать»).

import pandas

Библиотека хранится в переменной, через которую можно вызвать её методы. В сообществе принято давать ей короткое имя pd.

import pandas as pd

Эта команда означает «импортируй библиотеку Pandas как pd».

У нас есть набор данных, который нужно превратить в таблицу. Это делается вызовом конструктора DataFrame() (от англ. data frame, «структура данных»).

Конструктор принимает два аргумента – список данных и названия столбцов, которые должны быть в таблице. Например, если информация о столицах разных стран хранится в переменной atlas:

atlas = [  
    ['Франция','Париж'],  
    ['Россия','Москва'],  
    ['Китай','Пекин'],  
    ['Мексика','Мехико'],  
    ['Египет','Каир'],  
]

и нужно построить таблицу из двух столбцов country (страна) и capital (столица),

geography = ['country', 'capital']

синтаксис вызова конструктора DataFrame() выглядит так:

world_map = pd.DataFrame(data = atlas , columns = geography)

--- файл 05-03-02-dataframe ----


Обратите внимание, что DataFrame() – это конструктор библиотеки Pandas, поэтому перед именем конструктора стоит обращение к переменной, в которой библиотека хранится – pd.DataFrame().


atlas = [
    ['Франция','Париж'],
    ['Россия','Москва'],
    ['Китай','Пекин'],
    ['Мексика','Мехико'],
    ['Египет','Каир'],
]
geography = ['country', 'capital']
world_map = pd.DataFrame(data = atlas , columns = geography) # таблица сохраняется в переменной с произвольно выбранным именем world_map
print(world_map) # вывод на экран

В результате простой список пар страна-столица превратился в таблицу с индексами и именованными столбцами. Давайте создадим таблицу с данными о ваших музыкальных предпочтениях.

