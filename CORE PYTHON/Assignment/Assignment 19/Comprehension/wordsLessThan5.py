def wordLessThan5(text):
    return [word for word in text.split() if len(word)<5 ]


string = input("enter string :")
result = wordLessThan5(string)
print(f'word less than 5 charcater is : {result}')