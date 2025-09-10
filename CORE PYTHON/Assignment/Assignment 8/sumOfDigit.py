def sumDigit(n):
    temp=n
    sum=0
    while(temp>0):
        digit=temp%10
        temp=temp//10
        sum=sum+digit
    print(f'sum of digits of number is : {sum}')

n =int(input('enter a 3 digit number:'))
sumDigit(n)
