p =  int(input('Enter the Principle amount: '))
r =  int(input('Enter the Rate of interest: '))
n =  int(input('Enter Numbers fo times interest is compounded per year: '))
t =  int(input('Enter time in year: '))

# CI =p *(1 + r/100)**(n*t)
CI = p*(1+r/100)**n-p
print(f'The Compound Interest is {CI}')