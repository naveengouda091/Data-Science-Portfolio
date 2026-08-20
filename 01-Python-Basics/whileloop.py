'''
when we dont know number of repetations we use while loop 
in while loop initialization condition incremet or decrement are given in the saperate line
syntax

while(condition):
    code true
    incremnet/decrement

'''

# write a program to display the numbers from 10 to 20

# i=10
# while(i<=20):
#     print(i)
#     i=i+1


fact=1
i=int(input("enter a number"))
while(i>0):
    fact=fact*i
    i=i-1
print(fact)