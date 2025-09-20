def digitCount(num):
    if num == 0:
        return 0
    else:
        return 1+digitCount(num//10)
    
def powerSum(num, power):
    if num==0:
        return 0
    else:
        return (num % 10)**power + powerSum(num // 10,power)
    
def isArmstrog(num):
    digit = digitCount(num)
    return num == powerSum(num, digit)

n= int(input('enter number:'))
if isArmstrog(n):
    print(f'{n} is an armstrong number')
else:
    print(f'{n} is not armstrong number')