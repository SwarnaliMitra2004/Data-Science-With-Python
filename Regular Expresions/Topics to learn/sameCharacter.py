import re

words = [
    "civic",
    "trust",
    "widows",
    "maximum",
    "museums",
    "aa",
    "as"
]

pattern = r'^(.).*\1$'

for word in words:
    if re.match(pattern, word):
        print(word)