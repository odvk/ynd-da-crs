#�������������� ��������

#������4 / 4
#���������, ��� ����������, �������� ��� ����� ��������� ������ df ������� columns.

import pandas as pd
df = pd.read_csv('music_log.csv')

new_names = ['user_id', 'total_play_seconds', 'artist_name', 'genre_name', 'track_name']

df.set_axis(new_names, axis = 'columns', inplace = True)

print(df.columns)