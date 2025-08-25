t = int(input('Enter time:' ))

h = t // 3600
 
m = (t % 3600) // 60

s = t % 60

print(f' hours {h} : minut {m} : second {s}')

