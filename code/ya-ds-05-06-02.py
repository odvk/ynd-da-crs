#���������� � DataFrame
#������2 / 4
#���������� ����� ������������ ������ � ����� ���. ��� ����� ����� ����� ������������ ���������� ������� genre_fight['genre'] == 'pop'. ��������� ��������� � ���������� genre_pop. ����������� ����� �� ������ � ����� ����:
#����� ������������ ������ � ����� ��� ����� ...

import pandas as pd
df = pd.read_csv('music_log.csv')

genre_fight=df.loc[:,['genre', 'Artist']]

genre_pop = genre_fight.loc[genre_fight.loc[:,'genre'] == 'pop']['genre'].count()
print('����� ������������ ������ � ����� ��� �����',genre_pop)
