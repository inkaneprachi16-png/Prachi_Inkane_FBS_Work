string = input('enter a string:')
count = 1
for char in string:
    if char in ['a',' e', 'i', 'o' ,'u','A','E ', 'I', 'O', 'U']:
        count+=1

print('number of vowel in string:', count)