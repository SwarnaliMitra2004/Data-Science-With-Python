file = open("message.txt", "r")

lines = file.readlines()
totalLines = len(lines)

# Find meeting time
if totalLines <= 12:
    print("Meeting time is:", totalLines, "AM")
else:
    print("Meeting time is:", totalLines - 12, "PM")

# Convert all lines into words
words = []

for line in lines:
    words.extend(line.split())

# Find most frequent word
max_count = 0
meetingPlace = ""

for word in words:
    count = words.count(word)

    if count > max_count:
        max_count = count
        meetingPlace = word

print("Meeting place is:", meetingPlace, "Street")

file.close()