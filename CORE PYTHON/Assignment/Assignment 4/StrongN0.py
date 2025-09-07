n = int(input('enter number'))
temp = n
sum_of_factorials = 0

#digit seprate
while(temp>0):
    d = temp % 10

    #calculate factorial
    fact = 1
    for i in range(1, d+1):
        fact = fact*i

    sum_of_factorials += fact
    temp= temp// 10

if (sum_of_factorials == n):
    print(f'{n} is a strong number')
else:
    print(f'{n} is not strong number')