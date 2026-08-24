'''
range is ta method comes with three different formats. 

range with one parameter --- it starts fromm zero till the given value minus 1(x-1)
range with two parameters ---when we pass two parameters  first parameter to start the loop second parameter to end the loop. the end valuve will be -1 
range with three parameters --- first parameter start second parameter end value third parameter incremnet or decrement 
'''

'''
following examples demos loops with differ parameters
'''

# for i in range(5):
#     print(i)

# print("------------")
# for x in range(2,10):
#     print(x)

# print("------------")
# for y in range(10,0,-1):
#     print(y)


# for i in range(0,11,2):
#     # if (i%2==0):
#      print(i)


# num  = int(input("enter a number"))
# for i in range(1,num):
#     print(i*i)


# for i in range(50):
#     if (i%3==i%5):
#         print(f"{i}. hi hello ")


#     elif (i%3==0):
#         print(f"{i}. hi")

#     elif (i%5==0):
#         print(f"{i}. hello")

#     else :
#         print(f"{i}. not divisible by 3 or 5")

    



# for i in range(1,4):
#     for j in range(1,4):
#         print(i,j,end=" ")
#     print("\n")

# write a program to display the following patterns

"""
1.
*
* * 
* * *

2.
1
1 2
1 2 3

3.
1
2 2
3 3 3

4.
1
2 3
4 5 6

5.
*
* *
* * *
* *
*

"""


# Pattern 1
for row in range(1, 4):
	for column in range(row):
		print("*", end=" ")
	print()

print()


# Pattern 2
for row in range(1, 4):
	for number in range(1, row + 1):
		print(number, end=" ")
	print()

print()


# Pattern 3
for row in range(1, 4):
	for column in range(row):
		print(row, end=" ")
	print()

print()


# Pattern 4
number = 1
for row in range(1, 4):
	for column in range(row):
		print(number, end=" ")
		number = number + 1
	print()

print()


# Pattern 5
for row in range(1, 4):
	for column in range(row):
		print("*", end=" ")
	print()

for row in range(2, 0, -1):
	for column in range(row):
		print("*", end=" ")
	print()







