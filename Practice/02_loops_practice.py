# 04_loops_practice.py
# Practice 1: Print numbers 1...10
for i in range(1, 11):
    print(i)

# Practice 2: Sum of numbers 1...10
total = 0
for i in range (1, 11):
    total += i
print("Sum of numbers 1 to 10 is:", total)

# Practice 3: Right traingle pattern
n = 6
for row in range(1, n+1):
    line = ""
    for col in range(row):
        line += "*"
    print(line)

    #Practice 4: Factorical of 5

    #using for loop
    fact = 1
    for i in range (1, 6):
        fact *= i
    print("Factorial of 5 (for loop):", fact)

    # Uing while loop
    fact2 =1
    i = 1
    while i <= 5:
        fact2 *= i
        i += 1
    print("Factorial of 5 (while loop):", fact2)