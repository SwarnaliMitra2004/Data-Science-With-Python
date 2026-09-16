# Ask the user for the distance they want to travel
distance = float(input("How far would you like to travel in miles? "))

# Determine the best vehicle based on the distance
if distance < 3:
    print("I suggest Bicycle to your destination")
elif 3 <= distance < 300:
    print("I suggest Motor-Cycle to your destination")
else:
    print("I suggest Super-Car to your destination")