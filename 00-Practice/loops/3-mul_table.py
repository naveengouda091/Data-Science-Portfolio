x = int(input("enter a number: "))

i=1

while(i<11):
    print(f"{x} X {i} = {i*x}")
    i=i+1


for t in range(10,0,-1):
    print(f"{x} X {t} = {x*t}")
    t=t-1