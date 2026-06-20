        #LISTS

leaf = ["naruto", "sasuke", "sakura", "kakashi",]
sand = ["gaara", "temari", "kankuro", "deidara",]

#n= int(input("Enter a number between 0 and 3: "))

#print(leaf[n])
'''
for ninja in leaf:
    print(ninja)


for ninja in range(len(sand)):
    print(f"{ninja+1}: {sand[ninja]}")


'''
        #DICTS
'''
ninja={
    "naruto": "leaf",
    "sasuke": "leaf",
    "sakura": "leaf",
    "gaara": "sand",
    "temari": "sand",
    "kankuro": "sand"
}
'''
ninja=[
    {"name": "name", "village": "village", "CN": "chakra nature"},
    {"name": "naruto", "village": "leaf", "CN": "wind"},
    {"name": "sasuke", "village": "leaf", "CN": "lightning"},
    {"name": "sakura", "village": "leaf", "CN": "earth"},
    {"name": "gaara", "village": "sand", "CN": "wind"},
    {"name": "temari", "village": "sand", "CN": "wind"},
    {"name": "kankuro", "village": "sand", "CN": None }
]


# print(ninja["naruto"])
for ninjas in ninja:
    print(ninjas["name"], ninjas["village"], ninjas["CN"],sep=": ")