score=int(input("Enter your score: "))

if score>=90 and score<=100:#or 90<=score<=100: or score>=90: (if we assume that the score cannot be greater than 100)
    print("Your grade is A")

elif score>=80 and score<90:#or 80<=score<90: or score>=80: 
    print("Your grade is B")

elif score>=70 and score<80:#or 70<=score<80: or score>=70: 
    print("Your grade is C")

elif score>=60 and score<70:#or 60<=score<70: or score>=60: 
    print("Your grade is D")

else:# or elif score<60:
    print("Your grade is F")