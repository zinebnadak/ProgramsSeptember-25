#1 Write a program that reads in a positive integer n and prints all prime numbers that are less than or equal to n .
# write an algorithm of how you´ll solve this problem
# prime number is a number only divisible by 1 or itself

#Ask user for input "n"
#start a list to collect primenumbers up to n (included)
#Two for loops: first to go trough all numbers from 1-n, one by one. Second will actually test all numbers from 1-n to see if the number has a another divider. If so it is not a primenumber and will not be added to list
#print list of primenumbers as result

n = int(input("Enter an integer: "))

prime_num = []  # List to collect prime numbers

for i in range(2, n + 1):        # Start from 2 (1 is not prime)
    is_prime = True              # Assume i is prime
    for d in range(2, i):        # Check from 2 up to i-1
        if i % d == 0:
            is_prime = False     # Why work with range (2,i) and not starting from 1? Found a divisor → not prime. You're checking i % d == 0 for all d from 1 to i Every number is divisible by 1 and by itself → your condition is always true. So is_prime = False is set for every number
            break
    if is_prime:
        prime_num.append(i)      # Add to list only after checking all divisors

print(prime_num)







