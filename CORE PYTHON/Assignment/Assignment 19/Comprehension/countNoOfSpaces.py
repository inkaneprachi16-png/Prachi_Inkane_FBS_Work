def countSpace(string):
    return sum([1 for char in string if char == ' '])


string = input("enter string:")
result = countSpace(string)
print(f"number of spaces in strig is : {result}")
