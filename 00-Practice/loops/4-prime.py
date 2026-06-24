x = int(input("Enter a number: "))

for i in range(2,x):
    if(x%i == 0):
        print("number is not prime")
        break
else:
    print("number is prime")

    
