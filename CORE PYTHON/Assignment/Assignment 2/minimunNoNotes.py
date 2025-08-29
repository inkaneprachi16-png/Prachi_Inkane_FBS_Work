amount = int(input('enter the amount:'))

#define list of notes
notes = [2000,1000,500,200,100,50,20,10]

count = amount // notes
amount= amount % notes

print(f'minimum no. of notes for given amount is {amount}*{count}')




#  Note execte