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

c = """hi i am
       dinesh"""

print(c)
print(c[3])

for x in "dinesh":
    print(x)
    print(len(x))
    print("dinesh" in x)

name = "   dinsh    "
if "dinesh" not in name:
   print("dinesh is there")
else:
    print('no dinesh')
    
    
print(name[2:4])
print(name[:4])
print(name[4:])

print(name[-3:-1])
print(name.upper())
print(name.lower())
print(name.strip())
print(name.replace("d", "r"))

f = "hi, i am dinesh"
print(f.split(","))

exp = 1.5
text = f"my experience is {exp:.3f} years"
print(text)
print("hi, i am \"dinesh\"")