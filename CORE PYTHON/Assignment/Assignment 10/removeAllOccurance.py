li = [35,56,68,87,35,78,23,35,82,85]
new_list = []

for ele in li:
    if ele not in new_list:
        new_list.append(ele)

print('new list with removeing all occurances is :', new_list)


####not currect