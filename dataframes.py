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

# conditional data frames
booldf = df > 0
# passing the boolin value into the dataframe
df[booldf]
# shorter way to write it
df[df>0]
# then just one column
df['W']>0
# return a row in the dataframe
resultdf = df[df['Z']<0]
# chaining everything together
df[df['W']>0]['X']
# spilting up the steps
boolser = df['W']>0
result = df[boolser]
mycols = ['Y','X']
result[mycols]

# need to use & for and
df[(df['W']>0) & (df['Y'] > 1)]

# reseting index
df.reset_index()

newind = 'CA NY WY OR OC'.split()

df['States'] = newind

df.set_index('States')
