import numpy as np
import pandas as pd

d = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}

df = pd.DataFrame(d)

# droping missing data rows
df.dropna()

# filling na
df.fillna(value='FILL VALLUE')
