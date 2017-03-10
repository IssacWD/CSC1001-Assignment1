from math import sin
from math import cos
from math import tan
from math import pi

while True:
    tri = input("Input the trigonometric function:")
    if tri == 'sin':
        def func(x):
            return sin(x)
        break
    elif tri == 'cos':
        def func(x):
            return cos(x)
        break
    elif tri == 'tan':
        def func(x):
            return tan(x)
        break
    else:
        print("Please input one of 'sin' 'cos' 'tan'")

while True:
    A = input("Input the lower bound, a:")
    B = input("Input the upper bound, b:")
    if A <= B:
        a, b = float(A), float(B)
        break
    else:
        print("a <= b is required! Please input again")

while True:
    N = input("Input the number of subintervals, n:")
    if N.isdigit() and int(N) > 0:
        n = int(N)
        break
    else:
        print("n should be a positive integer! Please input again")

def integral(a, b, n):
    sum = 0
    for i in range(1, n+1):
        area = ((b - a) / n) * func(a + ((b - a) / n) * (i - 1 / 2))
        sum += area
    return sum
print(integral(a, b, n))