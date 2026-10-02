n=int(input("Enter the number oflines you want to read : "))
file=open("sample.txt","r")
for i in range(1,n+1):
    print(file.readline())
file.close()