import numpy as np
import pandas as pd

labels = ['a','b','c']
my_list = [10,20,30]
arr = np.array([10,20,30])
d = {'a' :10, 'b':20, 'c':30}

series = pd.Series(my_list, index=labels)

# can hold any data type
labeldata = pd.Series(data=labels)

ser1 = pd.Series([1,2,3,4],index=['USA', 'CHINA','FRANCE', 'GERMANY'])
ser2 = pd.Series([1,2,3,4],index=['USA', 'CHINA','ITALY', 'JAPAN'])

print(ser1['USA'])



