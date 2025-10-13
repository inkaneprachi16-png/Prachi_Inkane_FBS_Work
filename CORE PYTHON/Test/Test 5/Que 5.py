def union(list1, list2):
    union_list = []

    for i in list1:
        if i not in list1:
            union_list.append(i)

    for j in list2:
        if j not in list2:
            union_list.append(j)
            
    return union_list

list1 = [10,20,30,40]
list2 = [20,40,50,60]

print('first list:', list1)
print('second list:', list2)

list3 = list1+list2
print(f'union of two list is :{list3}')

union(list1, list2)