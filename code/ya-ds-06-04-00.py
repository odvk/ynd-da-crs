#4. �������������� ��������

import pandas as pd
df = pd.read_csv('music_log.csv')

measurements = [['������',146,152], # ��������� �������� � ������ ������� 
              ['����',0.36, 0.41], # measurements (����. measurement, ����������).
              ['��������',82, 217], 
              ['������',38, 261],
              ['����',56,401],
              ['������',588, 968],
              ['������',1195, 1660],
              ['����',2750, 3150],
              ['������', 4300, 4700],
              ['������ ������', 6, 5400]]
# �������� �������� �������� � ���������� header.
header = ['�������� ���� ','MIN', 'MAX'] 
# �������� ��������� ������ � ���������� celestial (����. celestial, ���������).
celestial = pd.DataFrame(data = measurements, columns = header)
print(celestial.columns)

celestial.set_axis(['celestial_bodies','min_distance','max_distance'], axis = 'columns', inplace = True)
print(celestial.columns)

print()
print(celestial)