#��������� ����������
#������6 / 8
#�������� ���������� �������� ������� 'genre_name', ����������� ����� unique(). ����������� ��������� � ������� �������� �����, ������� �������� �� ������ ����.

import pandas as pd
df = pd.read_csv('music_log_upd_nan.csv')

print(df['genre_name'].unique())
