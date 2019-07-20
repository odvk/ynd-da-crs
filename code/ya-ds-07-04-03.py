#Сортировка данных
#Задача3 / 5
#Кажется, предпочтения нашего меломана начинают проявляться. Но, возможно, длительность композиций от жанра к жанру сильно различается. Важно знать, сколько треков каждого жанра он включил.
#Сгруппируйте данные по столбцу genre_name и посчитайте, сколько значений в столбце genre_name. Сохраните результат в переменной count_music_user и выведите её значение на экран.
#Чтобы команда «распечатать сумму» из прошлой задачи не мешала рассматривать новое решение, закомментируйте её.

import pandas as pd
df = pd.read_csv('music_log_upd.csv')

genre_grouping = df.groupby('user_id')['genre_name']

def user_genres(group):
    for col in group:
        if len(col[1]) > 50:
            user = col[0]
            return user

search_id = user_genres(genre_grouping)

music_user = df[(df['user_id'] == search_id) & (df['total_play_seconds']>0)]
#print(music_user.head())

sum_music_user = music_user.groupby('genre_name')['total_play_seconds'].sum()
#print(sum_music_user)
#print()

# код ниже
count_music_user = music_user.groupby('genre_name')['genre_name'].count()
print(count_music_user)
