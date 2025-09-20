li1 = [1,2,3,4,5]
li2 = [5,6,7,8,3]

#convert list into set
set1 = set(li1)
set2 = set(li2)

#calculate union of list
union = list(set1 | set2)

print('union:', union)
