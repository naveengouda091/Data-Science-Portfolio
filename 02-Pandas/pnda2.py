import pandas as pd


data = {"a": 12, "b": 13, "c": 14}
index = ["e", "f", "g"]
series = pd.Series(data, index=index)
print(series)