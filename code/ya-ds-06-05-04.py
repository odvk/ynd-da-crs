#��������� ����������� ��������
#������4 / 6
#��������� ������������� �������� ������� 'artist_name' ������ unknown.

import pandas as pd
df = pd.read_csv('music_log_upd_col.csv')

df['track_name'] = df['track_name'].fillna('unknown')
df['artist_name'] = df['artist_name'].fillna('unknown')
