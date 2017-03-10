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
This programme will request a positive integer from the user and display the numbers of each digits of that integer in reverse order. The core code is:
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
