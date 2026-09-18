text = input("Enter a string : ")
if text.startswith("x"):
    text = text[1:]
if text.endswith("x"):
    text = text[:-1]

print(text)