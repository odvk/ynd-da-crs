#��������� ����������
#������3 / 8
#������� ���������. ����������� ����� reset_index() ��� ���������� ������� ��������.

import pandas as pd
df = pd.read_csv('music_log_upd_nan.csv')

shape_table = df.shape

df = df.drop_duplicates().reset_index(drop=True)