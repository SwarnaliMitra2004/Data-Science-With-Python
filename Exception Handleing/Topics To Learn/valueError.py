numbers = [10, -5, 20, -8, 15, -3, 7, -12, 25, -1]

try:
    index = int(input("Enter an index: "))
    number = numbers[index]

    if number > 0:
        print("Positive number")
    elif number < 0:
        print("Negative number")
    else:
        print("Zero")

except IndexError:
    print("Invalid index")