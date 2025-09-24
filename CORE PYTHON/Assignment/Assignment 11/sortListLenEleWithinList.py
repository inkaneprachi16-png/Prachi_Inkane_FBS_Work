li= ["collage", "university", "school", "coaching", "class"]

# Sort by length of each string
for i in range(len(li)):
    for j in range(i + 1, len(li)):
        if len(li[i]) > len(li[j]):
            li[i], li[j] = li[j], li[i]

print("Sorted by length:", li)
