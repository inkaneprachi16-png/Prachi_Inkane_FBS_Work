

age = int(input('enter the age of 1st person:'))
ticket_amount = int(input('enter the ticket amount:'))

if(age <12):
    total_amount = ticket_amount * (30/100)         #30% discount
elif(age>59):
    total_amount = ticket_amount * (50/100)         #50%discount
else:
    total_amount = ticket_amount                    #full pay


print(f'total ticket for 1st person is {total_amount} rs')

age = int(input('enter the age of 2nd person:'))
ticket_amount = int(input('enter the ticket amount:'))

if(age < 12):
    total_amount = ticket_amount * (30/100)
elif(age > 59):
    total_amount =  ticket_amount * ( 50/100)
else:
    total_amount = ticket_amount

print(f'total ticket of 2nd person is {total_amount}rs')


age  = int(input('enter the age of 3rd person: '))
total_amount = int(input('enter the ticket amount:'))

if(age < 12):
    total_amount = ticket_amount * (30/100)
elif(age > 59):
    total_amount = ticket_amount * (50/100)
else:
    total_amount = ticket_amount

print(f'total ticket of 3rd person is {total_amount}rs')


age = int(input('enter the age of 4th person:'))
total_amount = int(input('enter the ticket amount:'))

if(age < 12):
    total_amount = ticket_amount * (30/100)
elif(age > 59):
    total_amount = ticket_amount * (50/100)
else:
    total_amount = ticket_amount

print(f'total ticket of 4th person is {total_amount}rs')

age = int(input('enter the age of 5th person:'))
total_amount = int(input('enter the ticket amount:'))

if(age< 12):
    total_amount = ticket_amount * (30/100)
elif(age > 59):
    total_amount = ticket_amount * (50/100)
else:
    total_amount = ticket_amount

print(f' total ticket of 5th person is {total_amount}rs')