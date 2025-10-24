def nestedList():
    return [num for num in range(1, 1001) if any(num%d ==0 for d in range(1, 1001))]


li = nestedList()
print(li)