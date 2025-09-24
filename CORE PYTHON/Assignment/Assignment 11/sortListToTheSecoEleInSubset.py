
li = [[2, 4], [5, 2], [6, 9], [1, 0]]
for i in range(len(li)):
    for j in range(i + 1, len(li)):
        if li[i][1] > li[j][1]:                 #[1] → second element → used because we want to sort by the second item in each sublist.
            # Swap the sublists
            li[i], li[j] = li[j], li[i]

print("Sorted list:", li)