def removeVowel(text):
    vowel = 'aeiouAEIOU'
    return ''. join ([char for char in string if char not in vowel ])



string = input("enter string:")
result = removeVowel(string)
print(f'string without vowel is : {result}')