amount = int(input('enter the amount:'))

#calculate numbers of notes for each domination
notes_2000 = amount//2000
amount =  amount % 2000

notes_1000 = amount // 1000
amount = amount % 1000

notes_500 = amount // 500
amount = amount % 500

notes_200 = amount // 200
amount = amount % 200

notes_100 = amount // 100
amount = amount % 100

notes_50 = amount // 50
amount =  amount% 50

notes_20 = amount// 20
amount = amount%29

notes_10 = amount//10
amount = amount% 10

#print result
print('2000:', notes_2000, 'notes')

print('1000:', notes_1000, 'notes')

print('500:', notes_500, 'notes')

print('200:', notes_200, 'notes')

print('100:', notes_100, 'notes')

print('50:', notes_50, 'notes')

print('20:', notes_20, 'notes')

print('10:', notes_10, 'notes')
