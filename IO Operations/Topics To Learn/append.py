text = input("Enter the text you want to append : ")
file = open("sample.txt","a")
file.write(text + "\n")
file.close()