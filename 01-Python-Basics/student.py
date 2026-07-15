class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.house = house


    def __str__(self):
        return f"{self.name} from {self.house}"


    def charm(self):
        match self.house:
            case "Gryffindor":
                return "bravery"
            case "Hufflepuff":
                return "loyalty"
            case "Ravenclaw":
                return "devotion"
    @property     
    def house(self):
        return self.house




        
    

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.house = house



# def main():

#     student = get_student()
#     print(f"{student[0]} from {student[1]}")


# def get_student():
#     name = input("name: ")
#     house = input("house: ")
#     return (name, house)#tuple is immutable, so we can use it to return multiple values from a function. We can also use a list or a dictionary, but a tuple is more appropriate here since we don't need to modify the values.


# if __name__ == "__main__":
#     main()


def main():
    student = get_student()
    print(student)
    print("is known for their", student.charm())
   




def get_student():
    # student = {}
    # student["name"] = input("name: ")
    # student["house"] = input("house: ")
    # return student


    # student = Student()
    # student.name = input("name: ")
    # student.house = input("house: ")
    # return student

    name = input("name: ")
    house = input("house: ")
    return Student(name, house)
    




if __name__ == "__main__":
    main()


