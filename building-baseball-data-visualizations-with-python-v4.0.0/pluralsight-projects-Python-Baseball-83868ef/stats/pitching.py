import pandas as pd
import matplotlib.pyplot as plt

from data import games

plays = games.loc[(games['type'] == 'play')]
print(plays)
strike_outs = plays[plays['type'].str.contains('K')]
print(strike_outs)
