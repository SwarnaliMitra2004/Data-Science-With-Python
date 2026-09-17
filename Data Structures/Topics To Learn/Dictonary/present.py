dict ={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print(dict)
n =int(input("Enter the number to search : "))
if n in dict:
    print("present")
else:
    print("absent")