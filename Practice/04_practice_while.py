# number from 10 to 1
i = 10
while i >= 1:
    print(i)
    i -= 1

#print only even numbers 
i = 10
while i >= 2:
    print("only even numbers:", i)
    i -=2

# multiples of 3

i = 3
while i <= 30:
    print("multiples of 3:", i)
    i += 3

# multiples of 5 from 50 to 5

i = 50
while i >= 5:
    print("multiples of 5:", i)
    i -= 5

#squares of numbers from 1 to 10
i = 1
while i <= 10:
    print("squares of numbers from 1-10 are:", i**2)
    i += 1

#mu;tiples of 9 in the formact 9X1 = 9
i = 1
while i <= 12:
    print("9 x", i, "=", 9*i)
    i += 1

# Print numbers from 1 to 50 and express even and odd numbers (for loop)
for i in range(1, 51):
    if i % 2 == 0:
        print("even numbers:", i)
    else:
        print("odd number:", i)

#Write a for loop that prints numbers from 1 to 30, but:
#	•	If the number is divisible by 3, print "Fizz"
#	•	If the number is divisible by 5, print "Buzz"
#	•	If the number is divisible by both 3 and 5, print "FizzBuzz"(for loop)
for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Print numbers from 1 to 50 and express even and odd numbers (while loop)
i = 1
while i <= 50:
    if i % 2 == 0:
        print("even numbers", i)
    else:
        print("odd numbers:", i)
    i += 1

#Write a for loop that prints numbers from 1 to 30, but:
#	•	If the number is divisible by 3, print "Fizz"
#	•	If the number is divisible by 5, print "Buzz"
#	•	If the number is divisible by both 3 and 5, print "FizzBuzz"(while loop)
i = 1
while i <= 30:
    if i % 3 == 0 and i % 5 ==0:
        print("FixxBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    i += 1

# Write a loop that prints all numbers from 1 to 100, but:
#•	If a number is divisible by 4, print "Div by 4"
#•	If a number is divisible by 6, print "Div by 6"
#•	If a number is divisible by both 4 and 6, print "Div by 4 and 6"
#•	Otherwise, print the number itself (for loop)
for i in range(1, 101):
    if i % 4 == 0 and i % 6 == 0:
        print("Div by 4 and 6")
    elif i % 4 == 0:
        print("Div by 4")
    elif i % 6 == 0:
        print("Div ny 6")
    else:
        print(i)

# Write a loop that prints all numbers from 1 to 100, but:
#•	If a number is divisible by 4, print "Div by 4"
#•	If a number is divisible by 6, print "Div by 6"
#•	If a number is divisible by both 4 and 6, print "Div by 4 and 6"
#•	Otherwise, print the number itself (while loop)
i = 1
while i <= 100:
    if i % 4 == 0 and i % 6 == 0:
        print("Div by 4 and 6")
    elif i % 4 == 0:
        print("Div by 4")
    elif i % 6 == 0:
        print("Div ny 6")
    else:
        print(i)
    i += 1

#Write a for loop that prints numbers from 1 to 50, but:
#	•	If a number is divisible by 2 and 3, print "Div by 2 and 3"
#	•	If only divisible by 2, print "Div by 2"
#	•	If only divisible by 3, print "Div by 3"
#	•	Otherwise, print "Not divisible by 2 or 3"
for i in range (1, 51):
    if i % 2 == 0 and i % 3 == 0:
        print("Div by 2 and 3")
    elif i % 2 == 0:
        print("Div by 2")
    elif i % 3 == 0:
        print("Div by 3")
    else:
        print("Not divisible by 2 or 3")

#Write a for loop that prints numbers from 1 to 20, but only the odd numbers.
for i in range(1, 21, 2):
    print("Odd numbers:", i)

#Write a for loop that prints numbers from 1 to 30, but:
#	•	If divisible by 2 → print "Even"
#	•	If divisible by both → print "Div by 2 and 3"
#	•	Otherwise → print the number
for i in range(1, 31):
    if i % 2 == 0:
        print("even")
    elif i % 3 == 0:
        print("Div by 3")
    elif i % 2 == 0 and i % 3 == 0:
        print("Div by 2 and 3")
    else:
        print(i)

#Write a for loop that prints the squares of all even numbers from 1 to 20
for i in range(1, 21):
    print("square of", i, "is", i**2) 

#Write a for loop that prints numbers from 1 to 50, but:
#	•	If the number is divisible by 4, print the square of the number.
#	•	If the number is divisible by 7, print the cube of the number.
#	•	If divisible by both 4 and 7, print "Special" instead.
#	•	Otherwise, just print the number itself.
for i in range (1, 51):
    if i % 4 == 0 and i % 7 == 0:
        print("Special")
    elif i % 4 == 0:
        print(i**2)
    elif i % 7 == 0:
        print(i**3)
    else:
        print(i)

#Write a while loop that prints all odd numbers from 1 to 20.
i = 1
while i <= 20:
    print("odd numbers:", i)
    i += 2

#Write a while loop that prints numbers from 1 to 50, but:
#	•	If divisible by 4 → print "Div by 4"
#	•	If divisible by 6 → print "Div by 6"
#	•	If divisible by both → print "Div by 4 and 6"
#	•	Otherwise → print the number
i = 1
while i <= 50:
    if i % 4 == 0 and i % 6 == 0:
        print("Div by 4 and 6")
    elif i % 4 == 0:
        print("Div by 4")
    elif i % 6 == 0:
        print("Div by 6")
    else:
        print(i)
    i += 1

#Write a while loop that prints numbers from 1 to 30, but instead of printing them in a single column, print them in the format
#(That means 5 numbers per line)
i = 1
while i <= 30:
    print(i, end=" ")
    if i % 5 == 0:
        print()
    i += 1

#Write a while loop that prints numbers from 1 to 50, but shows them in rows of 7 numbers each
i = 1
while i <= 50:
    print(i, end=(" "))
    if i % 7 == 0:
        print()
    i += 1
    
# 5 per line with for loop
for i in range (1, 31):
    print(i, end=" ")
    if i % 5 ==0:
        print()