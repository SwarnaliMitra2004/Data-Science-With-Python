scores = [2, 3, 6, 5, 6]

unique = set(scores)

max1 = max(unique)

unique.remove(max1)

runner_up = max(unique)

print(runner_up)