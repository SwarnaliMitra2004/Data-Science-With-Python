def count_case(text):
    upper = 0
    lower = 0

    for ch in text:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1

    print("Uppercase:", upper)
    print("Lowercase:", lower)


text = input("Enter a string: ")

count_case(text)