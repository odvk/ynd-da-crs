#� ���� ���������� ������������
#������3 / 4
#���������� ���������� ������ �������� � ������ ������, ��������� ��������� � ���������� na_number. (�� ����. no answer number, ����������� ������������� ���� ��������). �������� � �������� �� �����.

import pandas as pd
df = pd.read_csv('music_log_upd.csv')

na_number = df.isna().sum()
print(na_number)

