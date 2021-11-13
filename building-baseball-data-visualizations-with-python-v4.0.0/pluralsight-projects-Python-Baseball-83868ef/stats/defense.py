import pandas as pd
import matplotlib.pyplot as plt

from frames import games
from frames import info
from frames import events

#plays = games.query()
games.info()
plays = games.query('type == "play" and event != "NP" ')

plays.columns = ['type','inning','team','player','count','pitches','event','game_id','year']
plays.info()

pa = plays.loc[plays['player'].shift() != plays['player'],['year','game_id','inning','team','player']]

pa.info()

pa = pa.groupby(['year','game_id','team']).size()
events = events.set_index(['year','game_id','team','event_type'])
events.unstack(level=0)
events.fillna(0)
events=events.reset_index()

events.info()
#events.columns = events.columns.droplevel()
