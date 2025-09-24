li = [5, 1, 9, 3, 7, 8]

# Bubble sort to sort the list
for i in range(len(li)):
    for j in range(len(li) - 1):
        if li[j] > li[j + 1]:
            li[j], li[j + 1] = li[j + 1], li[j]

# Second largest is at second last index after sorting
print("Second largest number is:", li[-2])