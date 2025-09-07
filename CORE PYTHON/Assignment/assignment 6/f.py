number = 1
for i in range(1, 6):
    for j in range(1, 10-i):
        print(' ', end =' ')

    for j in range(1, 2*i):
        print(j, end=' ')
    number +=1
    print()