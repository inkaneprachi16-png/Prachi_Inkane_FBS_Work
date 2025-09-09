for num in range(2,101):                
    for i in range(2, num//2+1):
            if(num % i==0):
                prime=False
                break
    else:
        print(num, end=' ')

