#7. ������ Series
#������� �������� � ����� ����� ����� � ������! ��� ������������ ����������, ������� ���������� ���� ������ ������� �� ����� 5 ������ � ����������: ������� �� �������� �������� ������� � �������� ����� �� ����� ��� �� ��� ������ ������ �������?

#������4 / 7
#�������� �� �������� ������� ������ ������ � ������ 'pop' � ��������� ��� ����� ������� � ���������� pop.
#����� ���������� ���������� ������ ���������������.

import pandas as pd
df = pd.read_csv('music_log.csv')

# <�������� ��� �����>
rock=df.loc[df['genre'] == 'rock']

rock_time=rock['total play']

rock_haters = rock_time.loc[rock_time <= 5].count()
#print('���������� ����������� ������ ����� ��� �����', rock_haters)

pop=df.loc[df['genre'] == 'pop']