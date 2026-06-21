def main():
    x=int(input("what's x: "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n%2==0:     #or return True if n%2==0 else return False
        return True #or return n%2==0
    else:
        return False

if __name__=="__main__":
    main()