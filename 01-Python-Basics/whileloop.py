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





temp = 0
digit_sum = 0
num = int(input("Enter a number: "))
while num > 0:
    temp = num % 10
    digit_sum = digit_sum + temp
    num = num // 10
print("Sum of digits:", digit_sum)


# Reverse a number
num = int(input("Enter a number to reverse: "))
original = num
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
print("Reverse:", reverse)


# Check whether a number is a palindrome
num = int(input("Enter a number to check for palindrome: "))
original = num
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome number")
else:
    print("Not a palindrome number")


# Check whether a number is an Armstrong number
num = int(input("Enter a number to check for Armstrong: "))
original = num
digits = 0
temp = num
while temp > 0:
    digits = digits + 1
    temp = temp // 10

armstrong_sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    armstrong_sum = armstrong_sum + digit ** digits
    temp = temp // 10

if original == armstrong_sum:
    print("Armstrong number")
else:
    print("Not an Armstrong number")