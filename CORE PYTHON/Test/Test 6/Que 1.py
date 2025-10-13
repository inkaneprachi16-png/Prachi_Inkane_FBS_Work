def notes(amount):
    total_notes = 0

    for note in D:
        if amount>=note:
            count = amount//note
            amount = amount% note
            print(f'note {note} :{count}')
            total_notes +=count
    print(f'Total notes = {total_notes}')



D = [2000, 500, 200, 100, 50, 20, 10, 5]
amount = int(input("enter the amount:"))
notes(amount)