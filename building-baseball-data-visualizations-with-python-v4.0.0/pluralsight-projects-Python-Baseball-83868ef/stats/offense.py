import pandas as pd
import matplotlib.pyplot as plt
from data import games
import re

plays = games.loc[(games['type'] == 'play')]
print(plays)
plays.columns = ['year','inning','team','player','count','pitches','event','game_id','year']
print(plays.describe())

hits = plays.loc[re.search(r"^(?:S(?!B)|D|T|HR)",plays['event']),['inning','event']]
