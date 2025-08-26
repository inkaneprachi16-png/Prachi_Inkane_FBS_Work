import random

ui = input('enter userid:')
pw = input('enter password:')

uid = 'admin'
passw = 'Pass123'

if(uid == ui and passw == pw):
    captcha = random.randint(1111,9999)
    print(f'Captcha: {captcha} ')
else:
    print(f'Uid and passw not verified')

captcha = int(input('enter the captcha:'))

if(captcha == captcha):
    print(f'massage success')
else:
    print(f'massage failed')

