start = int(input('enter the start of the range:'))
end = int(input('enter the end of the range:'))

for num in range(start , end+1):
    n = num
    temp = num

    #count number of digits
    count = 0
    while(temp>0):
        temp = temp//10
        count+=1


        #seprate digits
    temp = num
    sum_of_power = 0
    while(temp>0):
        digit = temp%10

        #calculate digit ** power using multiplication
        power = 1
        for i in range(count):       
            power = power *digit
        
        sum_of_power = sum_of_power + power
        temp = temp//10

    if (sum_of_power == n):
        print(n)


