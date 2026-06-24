
x, y, z = input("enter the numbers in order:").split()
x=int(x)
y=int(y)
z=int(z)



# x=int(input("what's x: "))
# y=int(input("what's y: "))
# z=int(input("what's z: "))


def great(x,y,z):
    if x>y>z:
        print("x is greater")
    elif y>x>z:
        print("y is greater")
    else:
        print("z is greater")

great(x,y,z)