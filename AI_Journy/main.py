#main.py

from calculator import add, subtract, multiply, divide

def demo():
    a, b = 12, 3
    print("a =", a, "b =" , b)
    print("add     :", add(a, b))
    print("subtract:", subtract(a, b))
    print("multiply:", multiply(a, b))
    print("divide  :", divide(a, b))

if __name__ == "__main__":
    demo()

