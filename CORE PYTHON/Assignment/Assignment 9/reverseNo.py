def reverseNo(n,rev=0):
    if (n==0):
        return rev
    else:
        digit = n% 10
        rev = rev*10+digit
        return reverseNo(n//10, rev)
    
n = int(input('enter  number:'))
result = reverseNo(n)
print(f'reverse of {n} is : {result}')