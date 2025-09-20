list = [12,6,89,18,98]
m = 2
n = 3
 
divisible_number=[]

for ele in list:
    if(ele % m == 0 and  ele % n == 0):
        divisible_number.append(ele)

print(f'the numbers which are divisible by {m}and {n} in the list is :{divisible_number}')


