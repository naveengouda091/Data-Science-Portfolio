def main():
    #print_column(4)
    #print_row(4)
    print_square(3)

def print_column(height):
    for i in range(height):
        print("#")

def print_row(width):
    print("?" * width)
'''
def print_square(size):
    for i in range(size):
        print("#" * size)

'''
def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()  # Print a newline after each row

main()

