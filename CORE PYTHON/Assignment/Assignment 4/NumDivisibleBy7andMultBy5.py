start_num = int(input('enter start number:'))
end_num = int(input('enter ending number:'))

i = start_num

while(i<=end_num):
    if(i%7 == 0 and i%5 == 0):
        print(i)
    i+=1