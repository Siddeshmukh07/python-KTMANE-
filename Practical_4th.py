//ARRAY
numbers = [10, 20, 30, 40, 50]
float = [10.1, 20.3, 30.4, 40.5, 50.6]
double = [1020.1345, 2230.3658768, 3220.47879, 4022.5809, 5045.67568]
print(numbers)
print(float)
print(double)

//DIRECTORY
import os

os.mkdir("Rohit")

print(os.getcwd())

print(os.listdir())

os.rmdir("Rohit")

os.chdir("C:\\Users\\Dyp\\Desktop")

print(os.getcwd())
//FILE
file = open("data.txt", "w")
file.write("Hello Python")
file.close()

file = open("data.txt", "r")
print("r mode:", file.read())
file.close()

file = open("data.txt", "a")
file.write("Welcome to Python")
file.close()

file = open("data.txt", "r+")
print("r+ mode:", file.read())
file.write("This is r+ mode")
file.close()

file = open("new.txt", "w+")
file.write("This is w+ mode")
file.seek(0)
print("w+ mode:", file.read())
file.close()

file = open("data.txt", "a+")
file.write("This is a+ mode")
file.seek(0)
print("a+ mode:", file.read())
file.close()
//MODULE
import math_module

result = math_module.add(10, 20)
print(result)
//package
import math
import random

num = random.randint(1, 100)

print("Square of the number:", math.sqrt(num))
//set
# 1. add()
s = {1, 2, 3}
s.add(4)
print(s)          # {1, 2, 3, 4}

# 2. remove()
s.remove(2)
print(s)          # {1, 3, 4}

# 3. discard()
s.discard(10)     # No error if 10 doesn't exist
print(s)

# 4. pop()
x = s.pop()
print(x)
print(s)

# 5. clear()
s.clear()
print(s)          # set()

# 6. union()
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b)) # {1, 2, 3, 4, 5}

# 7. intersection()
print(a.intersection(b))  # {3}

# 8. difference()
print(a.difference(b))    # {1, 2}

# 9. symmetric_difference()
print(a.symmetric_difference(b))  # {1, 2, 4, 5}

# 10. issubset()
c = {1, 2}
print(c.issubset(a))  
