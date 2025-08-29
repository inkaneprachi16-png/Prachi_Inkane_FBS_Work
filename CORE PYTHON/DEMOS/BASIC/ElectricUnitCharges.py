unit = float(input('enter the electricity unit charges:'))

if(unit <50):                       #for first 50 unit
    bill = unit* 0.50
elif(unit<150):                     #for next 100 unit(50+100 = 150)
    bill = (50*0.50)+(unit *0.75)
elif(unit<250):                         #after next 100 unit(150+100)
    bill = (50*0.50)+(150*0.75)+(unit * 1.20)
else:
    bill = (50*0.50)+(150*0.75)+(250*1.20)+(unit*1.50)

surcharge = bill * 20/100               #20%
total_bill = bill+surcharge

    
print(f'total electricity bill is {total_bill}')