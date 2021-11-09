import pandas as pd
import matplotlib.pyplot as py
from data import games

print(games)

attendence = games.loc[(games['type'] == 'info') & (games['multi2'] == 'attendance'),['year','multi3']]
print(attendence.info())
attendence.columns = ['year','attendence']
print(attendence)

attendence.loc[:,'attendence'] = pd.to_numeric(attendence.loc[:,'attendence'])
