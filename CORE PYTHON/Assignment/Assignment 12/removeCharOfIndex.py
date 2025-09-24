string = input('enter a string:')

result = ' '

for index in range(len(string)):
    if ( index%2==0):
        result +=string[index]

print('a string after removing characher at odd index is :', result)