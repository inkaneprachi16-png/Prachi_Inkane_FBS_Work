start_num = int(input('enter starting number:'))
end_num = int(input('enter ending number:'))
divisor = int(input('enter number to check divisibility by :'))

i = start_num

while(i<=end_num):
    if(i % divisor == 0):
        print(i)
    i+=1