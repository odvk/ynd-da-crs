#���������� ������
#������1 / 5
#����������� �������� Kepler ������ ������� �� ����� ������� � ������� �� ������ ������. � �� � ������ ������.������ ���������� �������� � ����������� �������. �� �� ���� �������� ������ 50 ����������.
#�������� ������� � ������������� �� �������.
#��� ����� ��������� �� ��������� ������ df ������, ���������� ����� ���� ��������:
#1) �������� � ������� 'user_id' ������ ���� ����� �������� ���������� search_id;
#2) ����� �������������, �.�. �������� � ������� 'total_play_seconds', �� ������ ��������� 0.
#��������� ��������� � ���������� music_user.

import pandas as pd
df = pd.read_csv('music_log_upd.csv')

genre_grouping = df.groupby('user_id')['genre_name']

def user_genres(group):
    for col in group:
        if len(col[1]) > 50:
            user = col[0]
            return user

search_id = user_genres(genre_grouping)

#��� ����

music_user = df[(df['user_id'] == search_id) & (df['total_play_seconds']>0)]
print(music_user)

