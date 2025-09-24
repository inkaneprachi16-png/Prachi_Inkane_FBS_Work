string = input('enter a string:')

lowercase_count = 0

for char in string:
    if char.islower():
        lowercase_count +=1

print('number of lowercase character in string is:', lowercase_count)