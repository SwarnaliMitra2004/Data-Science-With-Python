num1 = int(input("Enter a number : "))
num2 = int(input("Enter a number : "))

digit1=num1%10
digit2=num2%10
if digit1==digit2:
    print("They both have same last number")