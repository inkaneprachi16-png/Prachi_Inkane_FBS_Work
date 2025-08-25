bs =int(input('inter basic salary:'))
da = 10    #10%
ta = 12     #12%
hra = 15/100    #15%

#calculate DA

DA = da/100 * bs            #10% = 10/100

#calculate TA

TA = ta/100 *bs             #12% = 12/100

#calculate HRA

HRA = hra/100 * bs

print(f'total salary is {bs + DA + TA + HRA}')
