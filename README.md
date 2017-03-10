# CSC1001-Assignment1
## Author: WD
## Date: Mar.10, 2017
This file is to introduce how the codes of Assignment 1 is running.
###Question1
This programme will request the user to three parameters in float or integer type: final value, annual interest rate, and number of years. Other types of input will raise ValueError. The core formula to calculate the initial value is:
```Python
InitialValue = FinalValue / (1 + InterestRate/100) ** Years
```
Then the initial value will be output. Results in terminal are shown:
```bash
bash-3.2$ python3 /users/apple/q1.py
Enter the final account value:1000
Enter the annual interest rate:4.25
Enter the number of years:5
812.1190197993631
```
for sample values 1000, 4.25, and 5.

###Question2
This programme will request a positive integer from the user and display the numbers of each digits of that integer in reverse order. Other types of input will raise ValueError. The core code is:
```Python
num = input('Enter an integer:')
for i in range(len(num)):
    print(num[len(num)-1-i])
```
For instance, when 2718 is input:
```bash
bash-3.2$ python3 /users/apple/q2.py
Enter an integer:2718
8
1
7
2
```

###Question3
This programme will request an integer m from the user and print the smallest number of n such that n^2 is larger than m. Other types of input will raise ValueError. The core code is:
```Python
n = 0
while n**2 <= m:
    n += 1
print(n)
```
Taking an example of m = 10, the result will be:
```bash
Enter an integer:10
4
```

###Question4
This programme allows the user to input a number N, and print a table with N rows and 3 columns. In the mth row, your program should output three numbers: m, m+1, and m^(m+1). The core code is:
```Python
m = 1
print("m   m+1  m**(m+1)")
while m <= int(N):
    print(m, ' ', m+1, '  ', m**(m+1)) 
    m += 1
```
For example, when the user inputs N = 5, your program should output the following:
```bash
bash-3.2$ python3 /users/apple/q4.py
Enter an integer N:5
m   m+1  m**(m+1)
1   2    1
2   3    8
3   4    81
4   5    1024
5   6    15625
```
Note that an approach to check if there is input error is used:
```Python
while True:
    N = input('Enter an positive integer N:')
    if N.isdigit() and int(N) > 0:
        break
    else:
        print("Invalid input! Please input a positive integer.")
```
For this reason, the programme will display "Invalid input! Please input a positive integer." and let the user to input again if the input number is not a positive integer. For example:
```bash
Enter an positive integer N:1.5
Invalid input! Please input a positive integer.
Enter an positive integer N:-50
Invalid input! Please input a positive integer.
Enter an positive integer N:
```

###Question5
This programme allows the user to input an integer N, and print all the prime numbers which are smaller than N. The core code is:
```Python
n, count= int(N), 1
for p in range(2, n):
    if IsPrime(p):
        if count % 8 == 0:
            print(p)
        else:
            print(p, end=" ")
        count += 1
```
in which a function IsPrime(x) to verify a prime number is defined:
```Python
def IsPrime(x):
    i = 2
    while i < x:
        if x % i == 0:
            return False
        i += 1
    return True
```
For example, if 20 is input:
```Python
Enter an integer N:20
2 3 5 7 11 13 17 19
```
Note that if the input number is not a positive integer, the programme will display "Invalid input! Please input a positive integer." and please refer to Question4 for the code for it. For instance:
```
Enter an integer N:10.9
Invalid input! Please input a positive integer.
Enter an integer N:-4
Invalid input! Please input a positive integer.
Enter an integer N:
```

###Question6
This programme will approxiamte the value of integral of the trigonometric function (only sin, cos, or tan is available) input by the user above a certain interval [a, b] defined by the user. The core code is:
```Python
def integral(a, b, n):
    sum = 0
    for i in range(1, n+1):
        area = ((b - a) / n) * func(a + ((b - a) / n) * (i - 1 / 2))
        sum += area
    return sum
print(integral(a, b, n))
```
For example:
```bash
bash-3.2$ python3 /users/apple/q6.py
Input the trigonometric function:cos
Input the lower bound, a:0
Input the upper bound, b:500
Input the number of subintervals, n:100000
-0.467772292585137
```
Note that an approach to check the input error is used for the function, a, b, and n:
```
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
```
If invalid data is input, the results are as shown:
```bash
bash-3.2$ python3 /users/apple/q6.py
Input the trigonometric function:iii
Please input one of 'sin' 'cos' 'tan'
Input the trigonometric function:sin
Input the lower bound, a:8
Input the upper bound, b:2
a <= b is required! Please input again
Input the lower bound, a:2
Input the upper bound, b:8
Input the number of subintervals, n:1.9
n should be a positive integer! Please input again
Input the number of subintervals, n:100
-0.2706874040220319
```
