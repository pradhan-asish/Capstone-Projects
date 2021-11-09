import pandas as pd
import matplotlib.pyplot as plt

from data import games

plays = games.loc[(games['type'] == 'play')]
print(plays)
strike_outs = games[games['event'].str.contains('K')]
print(strike_outs)
strike_outs = strike_outs.groupby(['year','game_id'])
