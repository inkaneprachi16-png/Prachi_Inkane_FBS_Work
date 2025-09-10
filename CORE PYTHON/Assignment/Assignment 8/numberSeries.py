def numberSeries(num):
    sum=0
    for i in range(1,num+1):
        sum=sum+i
    print(f'sum of series 1+2+3+4+....+{num} is:{sum}')

num = int(input('enter number:'))

numberSeries(num)