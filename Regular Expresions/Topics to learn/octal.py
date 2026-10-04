import re

numbers = ['789', '123', '004']

for number in numbers:
    if re.fullmatch(r'[0-7]+', number):
        print(number, "is an octal number")
    else:
        print(number, "is not an octal number")