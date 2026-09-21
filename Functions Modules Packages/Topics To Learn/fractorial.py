def factorial(number):
    fact =1
    for i in range(1,number+1):
        fact = fact*i
    return fact
number = int(input("Enter a number :"))
result=factorial(number)
print("Factorial : ",result)