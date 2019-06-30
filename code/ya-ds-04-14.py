#14. Сокращения в условиях
#Прежде чем перейти к анализу фильмов по годам, рассмотрим несколько удобных сокращений.

#Напишем функцию, которая будет относить фильм к одной из трёх категорий: короткий, средний или длинный.
def length_category(length):
    if length > 130:
        return 'длинный'
    else:
        if length <= 130 and length > 120:
            return 'средний'
        else:
            return 'короткий'
			
#В этом коде есть вложенное условие. Избавиться от него можно ключевым словом elif (сокр. англ. else if, «иначе если»):
def length_category(length):
    if length > 130:
        return 'длинный'
    elif length <= 130 and length > 120:
        return 'средний'
    else:
        return 'короткий'
		
		
# Условие
# length <= 130 and length > 120
# также можно сократить:
# 120 < length <= 130

#В итоге функция выглядит так:
def length_category(length):
    if length > 130:
        return 'длинный'
    elif 120 < length <= 130:
        return 'средний'
    else:
        return 'короткий'

