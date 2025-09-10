def digit_count(num):
    count= 0
    while(num>0):
        num= num//10
        count+=1
    return count

def sum_of_pow(num, count):
    sum=0
    while(num!=0):
        rem=num%10
        sum = sum+(rem**count)
        num=num//10
    return sum

def isArmstrong(num):
    count=digit_count(num)
    sum = sum_of_pow(num, count) 
    if sum == num:
        print(f'{num} is armstrong number')  
    else:
        print(f'{num} is not armstrong number')

num= int(input('enter number'))
isArmstrong(num)
