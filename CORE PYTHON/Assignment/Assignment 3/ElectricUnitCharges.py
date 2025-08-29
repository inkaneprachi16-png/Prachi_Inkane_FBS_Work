unit = float(input('enter the electricity unit charges:'))

if(unit <50):                       #for first 50 unit
    bill = unit* 0.50
elif(unit<150):                     #for next 100 unit(50+100 = 150)
    bill = (50 * 0.50) + (unit - 100) *0.75
elif(unit<250):
    bill = (50 * 0.50)+(100 *0.75)+(unit-100)*1.20
else:
    bill = (50*0.50)+(100 * 0.75)+(100*1.20)+(unit-250)*1.50

surcharge = bill * 2/100
total_bill = bill +surcharge

print(f' electric bill include 20% is {total_bill}')