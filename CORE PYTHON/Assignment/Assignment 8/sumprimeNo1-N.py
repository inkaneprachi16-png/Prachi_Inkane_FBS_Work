# def prime(n):
#     for i in range(2, n//2+1):
#         if(n%i == 0):
#             print('not prime')
#     else:
#         print(' prime numbe')

# def sumOfPrime(n):
#         sum= 0
#         for i in range(2, n+1):
#                 if prime(n):
#                     sum = sum+i
#         return sum    

# n=int(input('enter number to find prime numbers:'))
# print(f'sum of prime number between 1-{n} is :{sumOfPrime(n)}')

























def sumPrime(num):
    sum=0
    for i in range(2, num+1):
        for j in range(2, num//2+1):
            if(i%j==0):
                break
        else:
            sum =sum+i
    print(f'sum of prime number betwwn 1 - {num} is :{sum}')

num = int(input('enter number :'))
sumPrime(num)          
        



