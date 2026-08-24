from numpy import random

x = random.randint(100, size=(5, 5))
print(x)


print("-------------------------------------------------")

y = random.rand(5)
print(y)

print("-------------------------------------------------")

z = random.choice([3, 5, 7, 9], size=(3, 3))
print(z)