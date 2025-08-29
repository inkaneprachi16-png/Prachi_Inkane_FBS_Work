sub1 = int(input('enter the marks of subject 1:'))
sub2 = int(input('enter the marks of subject 2:'))
sub3 = int(input('enter the marks of subject 3:'))
sub4 = int(input('enter the marks of subject 4:'))
sub5 = int(input('enter the marks of subject 5:'))

per = ((sub1+sub2+sub3+sub4+sub5)/500)*100
print(f'{per}%')

if(per>=75):
    print('o Grade')
elif(per<75 and per>=60):
    print('A Grade')
elif(per<60 and per>=46):
    print('B Grade')
elif(per<46 and per>=35):
    print('C Grade')
else:
    print('fail')