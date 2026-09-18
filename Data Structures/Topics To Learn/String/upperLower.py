text = input("Enter a string : ")
upper=0
lower=0
for ch in text:
    if ch.isupper():
        upper += 1
    else:
        lower +=1
print(upper)
print(lower)