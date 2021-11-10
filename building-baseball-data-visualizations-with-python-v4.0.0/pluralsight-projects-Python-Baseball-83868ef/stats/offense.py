import pandas as pd
import matplotlib.pyplot as plt
from data import games

plays = games.loc[(games['type'] == 'play')]
print(plays)
plays.columns = ['year','inning','team','player','count','pitches','event','game_id','year']
print(plays.describe())
