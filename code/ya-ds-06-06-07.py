#��������� ����������
#������7 / 8
#� ������� 'genre_name' �������� �������� '�����������' �� 'electronic' .

import pandas as pd
df = pd.read_csv('music_log_upd_nan.csv')

df['genre_name'] = df['genre_name'].replace('�����������', 'electronic')