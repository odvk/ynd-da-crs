#���������� � DataFrame
#������1 / 4
#�������� �������, ��������� �� �������� genre � Artist. ��������� � � ���������� genre_fight.

import pandas as pd
df = pd.read_csv('music_log.csv')

#print(df.info())

genre_fight=df.loc[:,['genre', 'Artist']]
