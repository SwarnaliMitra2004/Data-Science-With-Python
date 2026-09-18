n = int(input("Enter a number: "))

if n <= 1:
    print("Given number is not a prime number")
else:
   # is_prime = True

    for i in range(2, n):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
    #if is_prime:
        #print("Given number is a prime number")
    #else:
        #print("Given number is not a prime number")