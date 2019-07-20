#����������� ������
#������1 / 3
#�������� � ��� ����. ������ ������ ������������� user_id ������ �� ���. ��� ����� ����������� ������ �� ������� ������������, ����� ������� ����� ������������ �� ����������.

#������������ DataFrame �� ������� user_id, ��������� ���������� ��������� � ���������� genre_grouping (�� ����. genre, ����� � grouping, ������������).

#���������� ���������� ������, ������� ������� ������������, ������� count(), ������, ��� �������� ���� ������� genre_name. ��������� ��������� � ���������� genre_counting � �������� ������ 30 ����� ���� �������.

import pandas as pd
df = pd.read_csv('music_log_upd.csv')

genre_grouping = df.groupby('user_id')
genre_counting = df.groupby('user_id')['genre_name'].count()
print(genre_counting.head(30))
