text = "pen pencil pen bag tiffin bag"

words = text.split()  # Break the text into words

counts = {}  # Empty dictionary to store word counts

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

for word in counts:
    print(word, counts[word])