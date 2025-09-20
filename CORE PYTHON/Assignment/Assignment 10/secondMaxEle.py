li=[34,67,89,98,76,78,90]

max_num = 0
smax_num = 0

for ele in li:
    if(ele>max_num):
        smax_num= max_num
        max_num = ele
    elif(ele>smax_num):
        smax_num=ele

print(f'second max element in list is : {smax_num}')