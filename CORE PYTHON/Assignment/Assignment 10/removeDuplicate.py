li = [2,5,7,8,3,5,8,5,9,5,2,5 ]

new_list = []

for ele in li:
    if ele not in new_list:
        new_list.append(ele)
print('original list:',li)
print(f'after removing duplicates ele in list then new list is : {new_list}')