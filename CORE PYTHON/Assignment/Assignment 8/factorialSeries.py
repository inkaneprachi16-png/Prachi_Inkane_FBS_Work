def factorialSeries(n):
    sum=0
    fact=1
    for i in range(1,n+1):
        fact =fact*i
        sum=sum+fact
    print(f"Sum of the seies 1!+2!+3!+....{n}! is : {sum}")

n = int(input('enter number to find series:'))
factorialSeries(n)