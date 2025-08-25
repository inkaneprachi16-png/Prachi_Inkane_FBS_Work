d =  int(input('Enter the days: '))

y = d // 365
d = d % 365

w = d // 7
d = d % 7

print(f'Given days are converted in {y}year, {w}weeks, {d}days')



