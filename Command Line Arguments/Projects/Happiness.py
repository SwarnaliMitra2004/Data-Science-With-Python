import sys
like = set(sys.argv[1].split("-"))
dislike = set(sys.argv[2].split("-"))
numbers = sys.argv[3].split("-")

happiness=0

for num in numbers:
    if num in like:
        happiness +=1
    elif num in dislike:
        happiness -=1
print(happiness)
