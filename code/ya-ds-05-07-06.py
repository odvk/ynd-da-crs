#7. ������ Series
#������� �������� � ����� ����� ����� � ������! ��� ������������ ����������, ������� ���������� ���� ������ ������� �� ����� 5 ������ � ����������: ������� �� �������� �������� ������� � �������� ����� �� ����� ��� �� ��� ������ ������ �������?

#������6 / 7
#����� �� �������� � ����� ���������� � Series, �� ��� ��� pop_time, ����� ��������� ���������� ����������� � ������� 5 ������ ������ ����� ���. ����������� ������� pop_time <= 5. ��������� ��������� � ���������� pop_haters � ����������� �� ������ � ����� ����:
#���������� ����������� ������ ����� ��� ����� ...
#����� ������ � ���� ���������������.

import pandas as pd
df = pd.read_csv('music_log.csv')

# <�������� ��� �����>
rock=df.loc[df['genre'] == 'rock']
rock_time=rock['total play']

rock_haters = rock_time.loc[rock_time <= 5].count()
#print('���������� ����������� ������ ����� ��� �����', rock_haters)

pop=df.loc[df['genre'] == 'pop']
pop_time=pop['total play']
pop_haters = pop_time.loc[pop_time <= 5].count()
print('���������� ����������� ������ ����� ��� �����', pop_haters)
