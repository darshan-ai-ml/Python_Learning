#mport math and use sqrt, pow, and factorial.

import math

def demo():
    n = 16
    root = math.sqrt(n)
    power = math.pow(2, 5)
    fact = math.factorial(6)

    print(f"n = {n}")
    print(f"sqrt({n}) = {root}")
    print(f"2^5 (math.pow) = {power}")
    print(f"6! = {fact}")

if __name__ == "__main__":
    demo()