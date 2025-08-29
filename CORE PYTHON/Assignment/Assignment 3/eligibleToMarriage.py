

gender = input('enter gender (m/f):' )
age = int(input('enter age:'))

if(gender == 'm'):
    if(age>= 21):
        print("eligible for marriage") 
    else:
        print("not eligible for marriage")

else:
    if(age>= 18):
        print("eligible for marriage") 
    else:
        print("not aligible for marriage")            