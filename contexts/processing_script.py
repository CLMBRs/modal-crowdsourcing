import json
import pandas as pd
import numpy as np

d = pd.read_json('default.json')

exp = pd.unique(d['Expression'])

np.array(exp).tofile('default_modals.csv',sep=',')
