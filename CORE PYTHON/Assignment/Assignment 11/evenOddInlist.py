li=[34,55,66,78,98,4,46,33]

even_list = []
odd_list = []

for num in li:
    if num%2==0 :
        even_list.append(num)
    else:
        odd_list.append(num)

print(f'even numbers are {even_list}')
print(f'odd numbers are {odd_list}')