# import csv


# '''
# names = []

# for i in range (3):
#     names.append(input("what's your name: "))

# for name in sorted(names):
#     print(f"Hello, {name}")

# '''

# #name=input("what's your name: ")


# '''
# file=open("names.txt","a")
# file.write(f"{name}\n")
# file.close()
# '''



# '''
# with open("names.txt","a") as file:
#     file.write(f"{name}\n")
# '''    
# '''
# with open("names.txt","r") as file:
#     lines=file.readlines()

# for line in lines:
#     print("Hello, ", line.rstrip())
# '''
# '''   
# with open("names.txt","r") as file: #not efficient when sorting
#     for line in file:
#         print("Hello, ", line.rstrip())  
# ''' 
# '''
# names = []

# with open("names.txt") as file:
#     for line in file:
#         names.append(line.strip())

# for name in sorted(names, reverse=True):
#     print(f"Hello, {name}")
# '''
# '''
# with open("names.csv") as file:
#     for line in file:
#         name,middle_name, surname = line.rstrip().title().split(",")
#         #m_n= middle_name.capitalize()
#         print(f"{name} {middle_name[0]} {surname}")
# '''




# names=[]

# '''
# with open("names.csv") as file:
#     for line in file:
#         name, middle_name, surname = line.rstrip().title().split(",")
#         nam ={"name":name ,"middle_name":middle_name[0], "surname":surname}
#         #nam["name"] = name
#         #nam["middle_name"] = middle_name
#         #nam["surname"] = surname
#         names.append(nam)#f"{name} {middle_name[0]} {surname}"
# '''

# #def get_name(nam):
#     #return nam["name"]

# with open("names.csv") as file:
#     reader=csv.reader(file)
#     for name,middle_name,surname in reader:
#         names.append({"name":name, "middle_name":middle_name, "surname":surname})

# #for nam in sorted(names, key=get_name):

# for nam in sorted(names, key=lambda nam: nam["name"]):
#     print(f"{nam['name']} {nam['middle_name']} {nam['surname']}")



import csv

name=input("what's your name: ")
home=input("what's your home: ")

# with open("names.csv","a") as file:
#     writer=csv.writer(file)
#     writer.writerow([name,home])

with open("names.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})

