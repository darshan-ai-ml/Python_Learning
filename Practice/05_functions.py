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



