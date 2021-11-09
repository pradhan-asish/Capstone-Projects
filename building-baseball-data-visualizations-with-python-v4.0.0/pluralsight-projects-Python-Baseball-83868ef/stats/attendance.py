import pandas as pd
import matplotlib.pyplot as py
from data import games

print(games)

attendance = games.loc[(games['type'] == 'info') & (games['multi2'] == 'attendance'),['year','multi3']]
print(attendance.info())
attendance.columns = ['year','attendance']
print(attendance)

attendance.loc[:,'attendance'] = pd.to_numeric(attendance.loc[:,'attendance'])

py.plot(attendance['year'],attendance['attendance'])

py.plot(figsize=(15,7),kind='bar')
py.xlabel('Year')
py.ylabel('Attendance')
py.show()
