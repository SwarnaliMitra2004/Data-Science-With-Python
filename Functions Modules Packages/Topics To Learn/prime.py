def check_prime(number):
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


number = int(input("Enter a number: "))

if check_prime(number):
    print("Prime")
else:
    print("Not prime")