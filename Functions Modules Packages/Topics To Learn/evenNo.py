def even_numbers(numbers):
    result=[]
    for number in numbers:
        if number%2==0:
            result.append(number)
    print("Even numbers are : ",result)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers(numbers)