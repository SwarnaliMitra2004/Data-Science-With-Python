import nameFunction

name =input("Enter your name : ")
print(nameFunction.ispalindrome(name))
vowels =nameFunction.count_the_vowels(name)
print("No of vowels : ",vowels)
frequncy =nameFunction.frequency_of_letters(name)
print("Frequency of letters : ",end="")
result =[]
for letter,count in frequncy.items():
    result.append(letter+"-"+str(count))
print(",".join(result))
