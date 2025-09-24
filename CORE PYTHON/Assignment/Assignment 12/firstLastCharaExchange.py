
string = input("Enter a string: ")

# Count length
length = 0
for c in string:
    length += 1

if length < 2:
    print("Result:", string)
else:
    first = string[0]
    last = string[length - 1]
    
middle = ""
i = 1
while i < length - 1:
    middle += string[i]
    i += 1

result = last + middle + first
print("after swaping first and last charaher of string:", result)


