#���������� � DataFrame
#������3 / 4
#������ ���������� ����� ������������ ������ � ����� ���. �������� � ��� �������, ������� �� ����������, ������ � ���������� �������� df['genre'] == 'rock'. ��������� ��������� � ���������� genre_rock. ����������� ����� �� ������ � ����� ����:
#����� ������������ ������ � ����� ��� ����� ...

import pandas as pd
df = pd.read_csv('music_log.csv')

genre_fight=df.loc[:,['genre', 'Artist']]

genre_pop = genre_fight.loc[genre_fight.loc[:,'genre'] == 'pop']['genre'].count()
print('����� ������������ ������ � ����� ��� �����', genre_pop)

genre_rock = genre_fight.loc[genre_fight.loc[:,'genre'] == 'rock']['genre'].count()
print('����� ������������ ������ � ����� ��� �����', genre_rock)

