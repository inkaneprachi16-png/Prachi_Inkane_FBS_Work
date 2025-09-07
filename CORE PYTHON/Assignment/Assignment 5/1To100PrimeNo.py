for num in range(2,101):                    #startinf 2  because 1 is not prime
    prime = True

    for i in range (2, num):
        if(num % i == 0):
            prime = False
            break
    if prime:
        print(num, end =' ')
