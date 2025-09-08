n = int(input('enter number of term:'))

print('Geometric series with ratio 2:')

for i in range(n):
    term = 2**i
    sum_term = (2**i)-1
    print(term, end=' ')
print()
print('the sum of the geometric series is :', sum_term)
    
print()