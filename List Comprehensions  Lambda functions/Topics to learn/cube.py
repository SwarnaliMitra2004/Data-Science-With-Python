list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

cube = lambda x: x ** 3

result = list(map(cube, list_1))

print(result)