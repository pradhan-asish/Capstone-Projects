import pandas as pd
import matplotlib.pyplot as plt
from data import games
import re

plays = games.loc[(games['type'] == 'play')]
print(plays)
plays.columns = ['year','inning','team','player','count','pitches','event','game_id','year']
print(plays.describe())

hits = plays.loc[(plays['event'].str.contains(pat ='^(?:S(?!B)|D|T|HR)',regex = True )),['inning','event']]

hits.loc[:,'inning'] = pd.to_numeric(hits.loc[:,'inning'])

replacements = {r'^S(.*)': 'single',r'^D(.*)': 'double',r'^T(.*)': 'triple',r'^HR(.*)': 'hr'}

hit_type = hits['event'].replace(replacements,regex=True)

hits=hits.groupby(['inning','event']).size()
hits = hits.reset_index(name = 'count')
print(hits)

pd.Categorical( hits['hit_type'] : ['single','double','triple','hr'])
