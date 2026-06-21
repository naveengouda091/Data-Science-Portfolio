'''
try:
    x=int(input("what's x? "))
except ValueError:
    print("x is not a integer")
else:
    print(f"x is {x}")
'''


def main():
    x=get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x=int(input("what's x? "))
        except ValueError:
            #pass            
            print("x is not a integer")
        else:
             return x 

 
main()
