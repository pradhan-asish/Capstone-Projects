import os
import glob
import pandas as pd


game_files = glob.glob(os.path.join(os.getcwd(),'games','*.EVE'))
print(os.path.join(os.getcwd(),'games','*.EVE'))
print(game_files)
game_files.sort()
