#��������� ����������
#������8 / 8
#������� ���������: ������������ ���������� �������� '�����������' � ������� 'genre_name'. ���� ������� �� ��������, ��������� ������ ���� ����� 0. ��������� ���� ��������� � ���������� genre_final_count (�� ����. final count, �������������� �������), �������� �� �����.

import pandas as pd
df = pd.read_csv('music_log_upd_nan.csv')

df['genre_name'] = df['genre_name'].replace('�����������', 'electronic')

genre_final_count = df[df['genre_name'] == '�����������']['genre_name'].count()
print(genre_final_count)
