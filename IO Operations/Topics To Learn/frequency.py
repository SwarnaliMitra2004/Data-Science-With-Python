file=open("sample.txt",'r')
content =file.read()
words=content.split()
search_word = input("Enter the word you want to search: ")
count = 0
for word in words:
    if word==search_word:
        count += 1
print(count)
file.close()