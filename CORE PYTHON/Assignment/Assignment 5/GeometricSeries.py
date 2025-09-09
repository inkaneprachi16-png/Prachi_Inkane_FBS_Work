n = int(input('enter number of term:'))

print('Geometric series with ratio 2:')

for i in range(n):
    term = 2**i
    sum_term = (2**i)-1
    print(term, end=' ')
print()
print(f'the sum of the geometric series a+ar+ar^2=ar^3+...+ar^n-1 for {n} is : {sum_term}')
    
