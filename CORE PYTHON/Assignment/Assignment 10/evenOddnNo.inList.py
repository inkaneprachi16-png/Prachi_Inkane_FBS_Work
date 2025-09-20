li = [34,55,89,2,6,90,35,27]
even_list = []
odd_list = []

for ele in li:
    if (ele % 2 == 0):
        even_list.append(ele)
    else:
        odd_list.append(ele)

print('even list is :',even_list)
print('odd list is :',odd_list)