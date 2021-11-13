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
