string = input('enter a string:')

letter_count =0
digits_count = 0

##count letter
for char in string:
    if char.isalpha():
        letter_count+=1

##count digits
for char in string:
    if char.isdigit():
        digits_count+=1

print('numbers of letter in string is:', letter_count)
print('numbers of digits in string is :', digits_count)