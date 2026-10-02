file=open("sample.txt","r")
content =file.read()
words=content.split() #here delimeter is white space
longest=''
for word in words:
    if len(word) >len(longest):
        longest=word
print(longest)
file.close()