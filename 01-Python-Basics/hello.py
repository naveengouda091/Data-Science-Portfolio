#def is a keyword in Python used to define a function. A function is a reusable block of code that performs a specific task. The syntax for defining a function is as follows:

#def hello(to="World"):
    #print("Hello,",to)

#hello() 


#name=input("Enter your name: ").strip().title()
     #string-methods
     #.strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)
#name=name.strip()

    #.capitalize() method converts the first character of a string to uppercase and the rest to lowercase.
#name=name.capitalize()

      #.title() method converts the first character of each word to uppercase and the rest to lowercase.
#name=name.title()

     #split() method splits a string into a list where each word is a list item. By default, it splits on whitespace.
#first,last = name.split() 

     #f-string used in speical cases where we want to include variables inside a string. It is a more readable and concise way to format strings in Python.
   #hello(name) is a function call that executes the hello function defined earlier, passing the variable name as an argument. This will print "Hello, World!" followed by the value of name.

#print(f"Hello {first}")
#print(f"Hello {last}")

#hello(name)  


def main():
     name=input("enter your name:")
     hello(name)

def hello(to="world"):
     print("Hello,",to)

main()
hello()



