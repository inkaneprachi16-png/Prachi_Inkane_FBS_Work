def factor(n):
    # fact = 1
    
    for i in range(1, n+1):
        if(n%i==0):
            print(i, end = ' ')

n = int(input('enter number to find factors:'))
factor(n)