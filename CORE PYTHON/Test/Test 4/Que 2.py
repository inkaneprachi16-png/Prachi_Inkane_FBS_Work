def factorial(n):
    fact = 1

    if(n==0):
        return 1
    else:
        return n *factorial(n-1)
n = int(input('enterr number to find factorial:'))
print(factorial(n))