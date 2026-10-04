import string

result = {letter: i for i, letter in enumerate(string.ascii_lowercase, 1)}

print(result)