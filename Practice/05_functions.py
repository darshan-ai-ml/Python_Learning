#Functions 
# Define the function first

#basic
def greet():
    print("Hello")
greet()

#function basic_02
def greet():
    print("Hello I'm Darshan")
greet()

#function basic_03
def greet():
    print("Welcome to python functions!")
greet()

#functions with parameters
def greet(name):
    print("Welcome to python functions,", name)
greet("Darshan")

#functions with 2 parameters
def greet(name, age):
    print("Welcome to python functions,", name, "You are", age, "years old")
greet("Darshan", 23)

#function with return
def greet(name):
    return f"Hello {name}, How are you!"

result = greet("Darshan") #call the funcion
print(result)

#function with return_02
def greet(name, age):
    return f"Welcome to python functons, {name}! You are {age} years old."

msg = greet("Darshan", 23)
print(msg)

#Write a function called add_numbers(a, b) that returns the sum of a and b.
def add_numbers(a, b):
    return a + b
result = add_numbers(10, 20)
print(result)

#Write a function called multiply(a, b) that returns the product of a and b.
def multiply(a, b):
    return a*b

result = multiply(4, 6)
print(result)

#Write a function called calculate(a, b) that:
#	•	Returns two values → the sum and the product.
def calculate(a, b):
    sum_result = a + b
    product_result = a * b
    return sum_result, product_result
    
s, p = calculate(5, 3)
print("Sum:", s)
print("Product:", p)

#Write a function called stats(a, b) that returns 3 values:
#	•	the sum of a and b
#	•	the difference (a - b)
#	•	the product (a * b)
def stats(a, b):
    sum_result = a + b
    dif_result = a - b
    product_result = a * b
    return sum_result, dif_result, product_result

s, d, p = stats(10, 4)
print("Sum:", s)
print("Difference:", d)
print("Product:", p)

#Functions using default parameters
def greet(name="Hubby", age=23):
    return f"Hello {name}, you are {age} years old!"

msg1 = greet()
msg2 = greet("Darshan", 24)

print(msg1)
print(msg2)

#Write a function introduce(name="Darshan", country="India") that returns:
#. My name is <name> and I am from <country>.
def introduce(name="Darshan", country="India"):
    return f"My name is {name} I am from {country}."

msg1 = introduce("Darshan", "India")
msg2 = introduce("ammu", "USA")

print(msg1)
print(msg2)

#Write a function bill(name, items=1, price=100) that:
#	•	name → customer’s name (must be passed)
#	•	items → number of items (default = 1)
#	•	price → price per item (default = 100)
#	•	It should return a string like this:
#Hello <name>, your total bill is <items * price> Rs.

def bill(name="Darshan", items=1, price=100):
    return f"Hello {name}, your total bill is {items * price} RS."

msg1 = bill("Darshan")
msg2 = bill("Ammu", 3)
msg3 = bill("Pehel", 2, 150)

print(msg1)
print(msg2)
print(msg3)

#Write a function called marksheet(name, m1=0, m2=0, m3=0) that:
#	•	Takes a student’s name and 3 subject marks (default = 0).
#	•	Calculates:
#	•	total = m1 + m2 + m3
#	•	average = total / 3
#	•	Returns two values: total and average.
def marksheet(name="Darshan", m1=0, m2=0, m3=0):
    total = m1 + m2 + m3
    average = total / 3
    return total, average 

t, avg = marksheet("Drashan", 80,90, 70)
print("Total:", t)
print("Average:", avg)

t2, avg2 = marksheet("Ammu", 50, 60)
print("Total:", t2)
print("Average:", avg2)

#Write a function square(x) that returns the square of a number.
#Write a function cube(n) that returns the cube of a number (n³).
#Example: cube(3) → 27.
# 05_functions.py - minimal verified version

def square(x):
    return x**2

def cube(x):
    return x**3

print("square(5) ->", square(5))
print("cube(3)   ->", cube(3))

#Can a function call another function? ✅ Yes.
#Example:

def square(x):
    return x**2
def double_square(y):
    return 2 * square(y)

print(double_square(3))

#Write a function triple_square(n) that uses the existing square() function and returns 3 times the square of n.
def square(x):
    return x**2

def double_square(y):
    return 2 * square(y)

def triple_square(z):
    return 3 * square(z)

print(triple_square(3))

#Write a function compare_numbers(n) that:
#	•	Calculates the square, cube, and triple square of n.
#	•	Returns all three values.
def square(x):
    return x**2

def cube(x):
    return x**3

def triple_square(x):
    return 3 * double_square(x)

def compare_numbers(n):
    s = square(n)
    c = cube(n)
    ts = triple_square(n)
    return s, c, ts

s, c, ts = compare_numbers(4)
print("square:", s)
print("Cube:", c)
print("Triple Square:", ts)

#Functions + Condition → e.g., check if a number is even or odd.
def chcek_odd_even(n):
    if n % 2 == 0:
        return f"{n} is even"
    else:
        return f"{n} is odd"
    
print(chcek_odd_even(7))
print(chcek_odd_even(10))

#write a function check_positive_negative(n) that returns:
#	•	"<n> is Positive" if number > 0
#	•	"<n> is Negative" if number < 0
#	•	"<n> is Zero" if number == 0
def check_prositive_negative(n):
    if n > 0:
        return f"{n} is positive"
    elif n == 0:
        return f"{n} is nutral"
    else:
        return f"{n} is negative"
    
print(check_prositive_negative(0))
print(check_prositive_negative(-10))
print(check_prositive_negative(20))

#a function that returns the sum of numbers from 1 to n.
def sum_upto(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

print(sum_upto(5))
print(sum_upto(10))

#Write a function sum_even_upto(n) that returns the sum of all even numbers from 1 to n.
def sum_even_upto(n):
    total = 0
    for i in range (2, n+1, 2):
        total += i
    return total

print(sum_even_upto(10))

#write a function sum_odd_upto(n) that returns the sum of all odd numbers from 1 to n?
def sum_odd_upto(n):
    total = 0
    for i in range(1, n+1, 2):
        total += i
    return total

print(sum_odd_upto(5))

#Write a function sum_divisible_by(n, k) that returns the sum of all numbers from 1 to n that are divisible by k.
def sum_divisible_by(n, k):
    total = 0
    for i in range(1, n+1):
        if i % k == 0:
            total += i
    return total 

print(sum_divisible_by(20, 5))




