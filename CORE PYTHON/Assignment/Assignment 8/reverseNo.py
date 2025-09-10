def reverseNo(num):
    number = num
    rev= 0
    while(number>0):
        digit = number % 10
        number=number//10
        rev=rev*10+digit
    print(rev)

num= int(input('enter number:'))
reverseNo(num)