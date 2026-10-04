try:
    n = int(input("Enter a number: "))

    if n <= 1:
        print("Given number is not a prime number")
    else:
        for i in range(2, n):
            if n % i == 0:
                print("Not Prime")
                break
        else:
            print("Prime")
except ValueError:
    print("Please enter a valid number.")