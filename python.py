print("hello world")
print(16)
print(16*2)
#python comments
#print("I am Dinesh", 18, "years old")
x = 10
y = str(10)
z = float(10)
print(x, y, z)
print(type(x))

a, b, c = "dinesh" , "rajesh" , "aswathi"
print( a, b, c)

x = y = z = "dinesh"
print(x, y, z)

development = ["frontend ", "backend ", "full stack "]
x, y, z = development
print(x+ y+ z + "are the development types")

x = "python"

def myfunc():
    x = "php"
    print(x, "is a great programming language")
myfunc()

print(x, "is a great programming language")

x = "python"

def myfunc():
    global x
    print(x, "is a great programming language")
myfunc()

print(x, "is a great programming language")

a = 20
a = float(20)
print (a)
print(type(a))

import random

print (random.randrange(1, 10))