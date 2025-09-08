n = int(input('enter the value of n:'))
total =0

for i in range(1, n+1):
    total= total+n**i

print(f'the sum of seies N+N^2+N^3+...N^N= {n} is:{total}')