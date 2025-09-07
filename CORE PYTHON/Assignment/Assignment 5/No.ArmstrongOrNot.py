num = int(input('enter number to check number is armstrong or not:'))

#count digit

temp = num
count = 0
while(temp>0):
    count+=1
    temp = temp//10

    #seprate digits
    temp = num
    sum_of_power = 0

    while(temp>0):
        digit = temp %10

        #calculate power using multiplication
        power = 1
        for i in range(count):
            power = power*digit

        sum_of_power +=power
        temp = temp//10

    if( sum_of_power == num):
        print(f'{num} is armstrong number:')
    else:
        print(f'{num} is armstrong number')