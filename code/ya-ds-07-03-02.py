#����������� ������
#������2 / 3
#���� �����, ��, ��� �� ���� ������� ������ 50 �����, ����� ����� ������� ������������. ����� ����� ������, ��������� ������������� ����������.
#�������� ������� user_genres, ������� ��������� ����� ����������� ��� ���� �������� group. ������� ������ ���������� ������, �������� � ��� �����������.
#� ������ ������ ��� �������� � ��� ������ � �������� 0 � ������ �������� � �������� 1.
#��������� ����� ������, � ������� ������ (������� � �������� 1) �������� ����� 50 ��������, ������� ���������� ��� ������, (�������� �������� � �������� 0).

import pandas as pd
df = pd.read_csv('music_log_upd.csv')

#def user_genres(group):
#    for col in group:
#        if # ��������� �������: ���� ����� ������� col � �������� 1 ������ 50, �����
#            user = # � ���������� user ����������� ������� col[0]
#            return user

def user_genres(group):
    for col in group:
        if len(col[1]) > 50:
            user = col[0]
            return user