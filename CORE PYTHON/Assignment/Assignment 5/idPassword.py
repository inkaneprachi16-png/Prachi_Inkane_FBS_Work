uid = 'admin'
passw = 'Pass@123'

for i in range(3):
    ui = input('enter userid:')
    password = input('enter password:')
    
    if(ui == uid and password == passw):
        print('login successful')
        break
    else:
        print('id or password incorrect, try again.')

else:
    print('To many time try, program terminate.')