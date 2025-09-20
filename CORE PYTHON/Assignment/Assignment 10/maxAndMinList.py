li = [44,78,99,56,90,34]

max_num = 0

for ele in li:
    if (ele>max_num):
        max_num =ele
print(f'maximum number in list is :{max_num}')


for ele in li:
    if (ele<max_num):
        min_num = ele

print(f'minimum number in list is :{min_num}')