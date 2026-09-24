import sys
prime_sum=0
for i in range(1,11):
    num =int(sys.argv[i])
    is_prime=True
    if num<2:
        is_prime=False
    else:
        for j in range(2,int(num**0.5)+1):
            if num%j==0:
               is_prime=False
               break 
    if is_prime:
        prime_sum+=num
print("Sum of prime numbers : ",prime_sum)
