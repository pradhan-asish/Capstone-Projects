import pandas as pd
import matplotlib.pyplot as plt

from data import games

plays = games.loc[(games['type'] == 'play')]
print(plays)
strike_outs = games[games['event'].str.contains('K')]
strike_outs=strike_outs.groupby(['year','game_id']).size()
print(strike_outs)
