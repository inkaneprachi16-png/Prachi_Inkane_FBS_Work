feet = int(input('enter the distance in feet:'))
inch = int(input('enter the distance in inches:'))

#feet to meter
f_t_m = feet*0.3048
print(f'given distance {feet}f = {f_t_m} m')

#feet to centimeter
f_t_cm =  feet* 30.48
print(f'given distance {feet}f = {f_t_cm}cm')


#inches to meter
i_t_m = inch*0.0254
print(f'given distance {inch}inch = {i_t_m} m')
 
#inches to centimeter
i_t_cm = inch*2.54
print(f'given distance {inch}inch = {i_t_cm}cm')
