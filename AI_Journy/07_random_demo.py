#Import random and generate 5 random numbers.

import random

def demo():
    floats = [random.random() for _ in range(5)]
    ints = [random.randint(1, 100) for _ in range(5)]
    items = list(range(1, 11))
    random.shuffle(items)

    print("5 random floats:", floats)
    print("5 randowm ints:", ints)
    print("shuffeled 1...10:", items)

if __name__ == "__main__":
    demo()