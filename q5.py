def IsPrime(x):
    i = 2
    while i < x:
        if x % i == 0:
            return False
        i += 1
    return True

while True:
    N = input('Enter an integer N:')
    if N.isdigit() and int(N) > 0:
        break
    else:
        print("Invalid input! Please input a positive integer.")

n, count= int(N), 1
for p in range(2, n):
    if IsPrime(p):
        if count % 8 == 0:
            print(p)
        else:
            print(p, end=" ")
        count += 1