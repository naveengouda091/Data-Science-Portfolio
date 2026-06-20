name=input("what's your name: ")
'''
match name:
    case "naruto":
        print("You are a ninja")
    case "sasuke":
        print("You are a ninja ")
    case "sakura":
        print("You are a ninja ")
    case "luffy":
        print("You are a pirate")
    case "zoro":
        print("You are a pirate")
    case _:
        print("who are you?")
        #OR
'''

match name:
    case "naruto" | "sasuke" | "sakura":
        print("You are a ninja")
    case "luffy" | "zoro":
        print("You are a pirate")
    case _:
        print("who are you?")



