import pandas as pd
data = [[1,2,3],[4,5,6],[7,8,9]]
series=pd.Series(data)
print(series)

series['2'] = 10
print(series)