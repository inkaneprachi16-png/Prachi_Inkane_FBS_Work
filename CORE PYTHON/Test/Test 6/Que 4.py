def countFrequencies(numbers):
    frequency = {}
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    return frequency

# Example usage:
num = [1,3,4,1,2,3,6,7,1,2,4]
result = countFrequencies(num)
print(result)