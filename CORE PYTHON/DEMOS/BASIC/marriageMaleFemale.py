m = int(input('enter the age of male:'))
f = int(input('enter the age of female:'))

if(m>=21):
    if(f>=18):
        print(f'both are able to marriage')
    else:
        print(f'she is  not able to marriage')
else:
    print(f'he is  able to marriage:')