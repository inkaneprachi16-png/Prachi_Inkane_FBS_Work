n = int(input('enter number:'))
i = 1
sum = 0
while(i<n):
    if(n %i == 0):
        sum = sum+i
    i = i+1
if(sum == n):
    print(f'{n} is perfect numer')
else:
    print(f'{n} is not perfect number')
