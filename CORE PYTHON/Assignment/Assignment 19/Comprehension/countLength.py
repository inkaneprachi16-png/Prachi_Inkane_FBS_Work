def countLengthWord(text):
    return {word : len(word) for word  in text.split()}


string = input("enter string :")
result = countLengthWord(string)
print('length of each word is :', result)