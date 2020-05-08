import numpy as np
import pandas as pd

from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5,4),['A','B','C','D','E'], ['W','X','Y','Z' ])


type(df['W'])

data = df[['W','Z']]

# adding a new column
df['new'] = df['W'] + df['Y']
# remove a column
df.drop('new', axis=1, inplace=True)
# getting one column
df[['Z']]
# getting row through location
df.loc['C']
# getting row through index
df.iloc[2]
# Putting together row and column
df.loc['B', 'Y']

df.loc[['A','B'], ['W','Y']]