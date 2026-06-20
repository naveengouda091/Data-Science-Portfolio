def main():
    x=int(input("Enter a number: "))
    print("x squired is:", sqr(x))
    print("x cubed is:", cube(x))
    print("x factorial is:", factorial(x))

def sqr(n):
    return n*n #return is used to send back the result of a function to the caller. In this case, it returns the square of the number n. When the function is called, it will compute n*n and return that value to where the function was called.
    #or retorn n**2
    #or return pow(n,2)

def cube(n):
    return n*n*n #or return n**3 or return pow(n,3)

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1) #recursive function is a function that calls itself. In this case, the factorial function calls itself with the argument n-1 until it reaches the base case where n is 0. The factorial of a number n is the product of all positive integers less than or equal to n. For example, factorial(5) will compute 5*4*3*2*1 which equals 120.
main()