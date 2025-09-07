amount = int(input('enter the amount:'))

for note in range(100, 0,-1):
    if(note == 100 or note == 50 or note == 20 or note == 10 or note == 5 or note == 2 or note == 1):
        count = amount//note
        if(count>0):
            print(f'note {note} :{count}')
        amount = amount%note
