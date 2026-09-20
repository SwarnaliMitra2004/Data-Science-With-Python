students = {
    "Krishna": [67, 68, 69],
    "Arjun": [70, 98, 63],
    "Malika": [52, 56, 60]
}

name = input("Enter a name: ")

marks = students[name]

average = sum(marks) / len(marks)

print("Average percentage mark:", average)