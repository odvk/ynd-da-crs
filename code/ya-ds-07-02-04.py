#� ���� ���������� ������������
#������4 / 4
#���������� ���������� ���������� � ������ ������, ��������� ��������� � ���������� duplicated_number (�� ����. duplicated number, ������ ����������). �������� � �������� �� �����.

import pandas as pd
df = pd.read_csv('music_log_upd.csv')

duplicated_number = df.duplicated().sum()
print(duplicated_number)