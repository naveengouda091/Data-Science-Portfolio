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


# fact=1
# i=int(input("enter a number"))
# while(i>0):
#     fact=fact*i
#     i=i-1
# print(fact)


'''
write a program to read a number and display it indivusual digits example 
246 =====  6 4 2
write a program to read a number and find the sum of indivusual digits  


write a pgm to read a num and reverse the same 

write a prgm to read a number and check is it a panadrome number

write a prgm to read a number an check is it a armstrong number 

'''


temp=0
sum=0
num=int(input("enter a number"))
while(num>0):
    temp=num%10
    sum=sum+temp
    num=num/10
print(sum)