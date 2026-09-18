text = input("Enter a string : ")
left =0
right =len(text)-1
while(left<=right):
    if text[left] != text[right]:
        print("Not palindrome")
        break
    left += 1
    right -=1
else:
    print("Palindrome")