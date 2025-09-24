str1 = input('enter a string 1:')
str2 = input('enter a string 2:')

##count length of string 1
count1= 0
for char in str1:
    count1+=1

###count length of string 2
count2 = 0
for char in str2:
    count2+=1



if (count1>count2):
    print('larger string is:', str1)
elif (count1<count2):
    print('larger string is :', str2)
else:
    print('both strigs are equal length')