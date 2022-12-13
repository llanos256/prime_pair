import numpy as np
import math
import time

##Method to get all prime numbers less than n
def getPrimeNumbers(n, prime):
    prime[0] = False
    prime[1] = False

    for i in range(2, n + 1):
        prime[i] = prime[i] = True

    for x in range(2, int(math.sqrt(n)) + 1):
        if prime[x] == True:
            for i in range(x * 2, n + 1, x):
                prime[i] = False

#It captures a prime pair
def getPair(n):
    found = False
    prime = [False] * (n + 1)
    getPrimeNumbers(n, prime)
    start = time.time()
    for i in range(2, n):
        j = int(n/i)

        if (prime[i] & prime[j] and j != i and j * i == n):
            print(n, ':', i, j)
            found = True
            break
    if not found:
        print('no pair found for', n)
    end = time.time()
    print('Execution time:', end - start, 'seconds')


print('How many test cases P =')
p = int(input())
if p >= 1000000:
    print('Invalid quantity')
else:
    ##array with random numbers for test cases
    k = np.random.randint(1000000, size=(p))
    for i in k:
       getPair(i)
