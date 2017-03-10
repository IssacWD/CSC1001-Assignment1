while True:
    N = input('Enter an positive integer N:')
    if N.isdigit() and int(N) > 0:
        break
    else:
        print("Invalid input! Please input a positive integer.")
m = 1
print("m   m+1  m**(m+1)")
while m <= int(N):
    print(m, ' ', m+1, '  ', m**(m+1)) 
    m += 1
