num_passanger = int(input('enter number of passangers:'))
ticket_cost = int(input('enter ticket cost:'))
total_amount = 0

for i in range(num_passanger):
    age = int(input('enter the age of passanger:'))

    if (age< 12):
        ticket = ticket_cost *30/100
    elif(age >59):
        ticket = ticket_cost * 50/100
    else:
        ticket = ticket_cost

    total_amount = ticket

print(f'total ticket amount to travel is {total_amount}')