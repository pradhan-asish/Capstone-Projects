import pandas as pd
import matplotlib.pyplot as py
from data import games

print(games)

atendence = games.loc[(games['type'] == 'info') & (games['multi2'] == 'attendence'),['type','multi2','year','multi3']]
