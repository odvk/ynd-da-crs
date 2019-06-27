#Простые функции
#Задача
#В таблице бюджеты указаны в долларах. Напишите функцию print_budget_in_rubles() (англ. print budget in rubles, «вывести бюджет в рублях»), которая переводит их в рубли и печатает на экране. Используйте курс 1$ = 67.01₽.

#Функция должна принимать сумму в долларах как аргумент и выводить на экран результат в формате:
#Бюджет: 13402.00 млн ₽
#Обратите внимание: сумма выводится с двумя знаками после запятой.

# Записываем курс в переменной rubles_for_dollar
# (англ. rubles for dollar, "рублей за доллар").
rubles_for_dollar = 67.01

def print_budget_in_rubles(dollars):
    rubles = dollars * rubles_for_dollar
    print('Бюджет: {:.2f} млн ₽'.format(rubles))

print('Титаник')
print_budget_in_rubles(200.0)
print()
print('Гладиатор')
print_budget_in_rubles(103.0)