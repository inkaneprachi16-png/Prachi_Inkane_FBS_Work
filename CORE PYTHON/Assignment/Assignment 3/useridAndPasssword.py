ui = input('enter the userid:')
pw = input('enter the password:')

uid = 'admin'
passw = 'abc@123'

if(uid == ui and passw == pw):
    print(f'uid and passw are correct')
else:
    print(f'uid and passw are incorrect')