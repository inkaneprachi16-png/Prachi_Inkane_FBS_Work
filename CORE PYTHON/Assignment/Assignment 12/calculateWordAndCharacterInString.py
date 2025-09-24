string = input('enter a string:')

##character count
char_count= 0
for char in string:
    char_count += 1


##count words

words = string.split()
words_count = 0
for words in words:
    words_count+=1


print('number of character in string is :', char_count)
print('number of words in string is :', words_count)