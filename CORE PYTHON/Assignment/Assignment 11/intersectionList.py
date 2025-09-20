li1 = [1 ,2 ,3, 4, 5]
li2 = [5,6,4,7,8]

#convert list into set
set1 =set(li1)
set2 = set(li2)

#calculate intersection of two list
intersection = list(set1 & set2)

print('intersecion:', intersection)