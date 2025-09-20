def fibbo(n,a, b):
    if (n>0):
        c= a+b
        print(c, end=' ')
        return fibbo(n-1, b,c)

n= int(input('enter number:'))
fibbo(n, -1, 1)