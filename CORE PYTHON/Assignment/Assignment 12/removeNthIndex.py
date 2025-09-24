
string = "FirsBit solution"
n = 5

# Check if index is valid
if n < 0 or n >= len(string):
    print("Index out of range.")
else:
    result = ' '
    i = 0
    while i < len(string):
        if i != n:
            result = result + string[i]
        i = i + 1
      
    print("Original String:", string)
    print("String after removing index", n, ":", result)