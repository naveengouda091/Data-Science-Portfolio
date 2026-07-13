def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("name: ")
    house = input("house: ")
    return (name, house)#tuple is immutable, so we can use it to return multiple values from a function. We can also use a list or a dictionary, but a tuple is more appropriate here since we don't need to modify the values.


if __name__ == "__main__":
    main()


