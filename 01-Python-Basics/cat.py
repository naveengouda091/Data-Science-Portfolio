        #LOOPS

'''
i=10
n=int(input("how many times do you want to meow? "))
y=i-n
while i > y:
    print(f"meow {10-i}")
    i = i - 1#or i -= 1
'''
#or
'''
i=0
n=int(input("how many times do you want to meow? "))

while i<n:
    print(f"meow {i+1}")
    i = i + 1#or i += 1
'''
'''
for i in [0,1,2,3,4]: #or for i in range(5):
    print(f"meow {i+1}")
'''
'''
for i in range(1,6):
    print(i)
'''
'''
print("meow \n"*5,end="") #or print("meow\n " * n)
'''

'''

while True:
    n=int(input("how many times do you want to meow? "))
    if n>0:
        break

for _ in range(n):
    print("meow")
'''

def main():
    x=get_number()
    meow(x)

def get_number():
    while True:
        n=int(input("how many times do you want to meow? "))
        if n>0:
            break
    return n
        

def meow(n):
    for _ in range(n):
        print(f"meow {_+1}")

main()
