numbers = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
result = []
for t in numbers:
    new_tuple = t[:-1] + (100,)
    result.append(new_tuple)
print(result)