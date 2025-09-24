rows = 10
cols = 10
num = 100

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(num)
        num -= 1

    # Reverse row on every other line to simulate zigzag (like a snake pattern)
    if i % 2 == 1:
        row.reverse()

    # Print the row
    for val in row:
        print(f"{val:3}", end=" ")
    print()
