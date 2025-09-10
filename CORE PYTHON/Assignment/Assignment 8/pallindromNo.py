def pallindromeNo(num):
    number=num
    rev=0
    while(num>0):
        digit = num% 10
        num =num//10
        rev = rev*10+digit

    return number==rev
num = int(input('enter number: '))
if pallindromeNo(num):
    print(f'{num} is pallindrome number')
else:
    print(f'{num} is not  pallindrome number')

    

    

