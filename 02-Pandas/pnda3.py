import pandas as pd


data={
    "Name": ["John", "Alice", "Bob"],
    "Age": [25, 30, 22],
    "City": ["New York", "Los Angeles", "Chicago"]
}

df= pd.DataFrame(data)
print(df)

print("-------------------------------------------------")

data1= [
    {"Name": "John", "Age": 25, "City": "New York"},
    {"Name": "Alice", "Age": 30, "City": "Los Angeles"},
    {"Name": "Bob", "Age": 22, "City": "Chicago","Country": "USA"}
]

df1= pd.DataFrame(data1)
print(df1)

print("-------------------------------------------------")


df1.drop("Country", axis=1, inplace=True)
print(df1)


print("-------------------------------------------------")

x = df1.at[2, "Age"]
print(x)

print("-------------------------------------------------")

x = df1.iat[2, 2]
print(x)