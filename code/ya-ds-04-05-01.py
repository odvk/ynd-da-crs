#Локальные и глобальные переменные
#Задача
#Создайте функцию minutes_to_hours() (англ. minutes to hours, «минуты в часы»): она должна переводить длительность фильма из минут в часы. Пусть на вход функция принимает длительность в минутах, а возвращает — в часах. Количество минут в часах запишите в константу MINUTES_IN_HOUR (англ. minutes in hour, «минут в часе»).

# создайте константу MINUTES_IN_HOUR

MINUTES_IN_HOUR = 60

def minutes_to_hours(minutes):
    hours = minutes /MINUTES_IN_HOUR
    return hours

print('Длина фильма "Форма воды": {:.2f} ч.'.format(minutes_to_hours(123)))
