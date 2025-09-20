li = [45,56,87,96,70,39,45]

ele= int(input('enter the number to check number is present or not in list:'))
count = 0

for num in li:
    if num == ele:
        count+=1

if count>0:
    print(f'the {ele} is present in list {count} time') 
else:
    print(f'the {ele} is not present in list')