import pandas as pd
import matplotlib.pyplot as py
from data import games

print(games)

atendence = games.loc[(games['type'] == 'info') & (games['multi2'] == 'attendance'),['year','multi3']]
print(atendence.info())
atendence.columns = ['year','attendence']
print(atendence)

atendence.loc[:,'attendence'] = pd.to_numeric(atendence.loc[:,'attendence'])
