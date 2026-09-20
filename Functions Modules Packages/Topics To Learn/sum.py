def sum(numbers):
    total =0
    for num in numbers:
        total += num
    return total
numbers = [8, 2, 3, 0, 7]
result = sum(numbers)
print(result)