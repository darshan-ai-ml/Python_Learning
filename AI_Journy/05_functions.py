#functions
def greet():
    print("Hello hubby ❤️, your wifey is teachng you Functions!")
greet()

#functions with parameters 
def greet(name):
    print("hello", name, "❤️ Your wifey is teaching you Functions")
greet("Darshan")

#Functions with return value
def add(a, b):
    return a + b

result = add(5, 3)
print("sum is:", result)

#Functions with multiple parameters
def introduce(name, age):
    return f"My name is {name} and I am {age} years old."

msg = introduce("Drashan", 23)
print(msg)

#Functions with dfault parameters

def greet(name="Hubby", age=23):
    return f"Hello {name}, you are {age} years old!"

msg1 = greet()
msg2 = greet("Darshan", 24)

print(msg1)
print(msg2)

#Functions returning muliple value 
def calculate(a, b):
    sum_result = a + b
    dif_result = a - b
    return sum_result, dif_result

s, d = calculate(10, 5)
print("sum:", s)
print("Difference:", d)



