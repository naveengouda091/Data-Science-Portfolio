# Read 5 numbers and display the greatest
numbers = []
for count in range(5):
	numbers.append(float(input("Enter a number: ")))
print("Greatest number:", max(numbers))


# Read 3 sides and display the type of triangle
side1 = float(input("Enter side 1: "))
side2 = float(input("Enter side 2: "))
side3 = float(input("Enter side 3: "))

if side1 <= 0 or side2 <= 0 or side3 <= 0:
	print("Invalid triangle")
elif side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
	print("Invalid triangle")
elif side1 == side2 == side3:
	print("Equilateral triangle")
elif side1 == side2 or side1 == side3 or side2 == side3:
	print("Isosceles triangle")
else:
	print("Scalene triangle")


# Read marks and display the result
marks = float(input("Enter marks: "))
if 75 <= marks <= 100:
	print("Distinction")
elif 60 <= marks < 75:
	print("First class")
elif 50 <= marks < 60:
	print("Second class")
elif 35 <= marks < 50:
	print("Pass")
else:
	print("Fail")


# Display a message based on divisibility by 3 and 5
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
	print("hi hello")
elif num % 3 == 0:
	print("hello")
elif num % 5 == 0:
	print("hi")


# Check whether a number is positive or negative
num = float(input("Enter a number: "))
if num > 0:
	print("Positive")
elif num < 0:
	print("Negative")
else:
	print("Zero")


# Check whether a number is divisible by 3
num = int(input("Enter a number: "))
if num % 3 == 0:
	print("Divisible by 3")
else:
	print("Not divisible by 3")


# Read 2 numbers and display the greatest
first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))
if first > second:
	print("Greatest number:", first)
elif second > first:
	print("Greatest number:", second)
else:
	print("Both numbers are equal")
