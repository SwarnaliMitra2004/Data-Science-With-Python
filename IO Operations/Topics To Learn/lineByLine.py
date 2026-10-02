file=open("sample.txt","r")
lines=file.readlines()
print(lines)
file.close()

#file.read()       # entire file → one string
#file.readline()   # one line → one string
#file.readlines()  # all lines → list of strings