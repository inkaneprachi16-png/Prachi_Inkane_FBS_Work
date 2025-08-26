unit = float(input('enter the electricity unit charges:'))

if(unit <50):                       #for first 50 unit
    bill = unit* 0.50
elif(unit<150):                     #for next 100 unit(50+100 = 150)
    bill = 