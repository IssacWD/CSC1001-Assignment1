FinalValue = float(input('Enter the final account value:'))
InterestRate = float(input('Enter the annual interest rate:'))
Years = float(input('Enter the number of years:'))

InitialValue = FinalValue / (1 + InterestRate/100) ** Years

print(InitialValue)