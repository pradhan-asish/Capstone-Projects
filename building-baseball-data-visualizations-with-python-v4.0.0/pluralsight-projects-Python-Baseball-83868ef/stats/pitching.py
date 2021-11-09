import pandas as pd
import matplotlib.pyplot as plt

from data import games

plays = games.loc[(games['type'] == 'play')]
print(plays)
strike_outs = games[games['event'].str.contains('K')]
strike_outs=strike_outs.groupby(['year','game_id']).size()
strike_outs = strike_outs.reset_index(name = 'strike_outs')
print(strike_outs)
strike_outs.loc[:,'year'] = pd.to_numeric(strike_outs.loc[:,'year'])
strike_outs.loc[:,'strike_outs'] = pd.to_numeric(strike_outs.loc[:,'strike_outs'])
