"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

import math

def primes(number_of_primes):
    list = []
    count = 2
    while len(list)<number_of_primes:
        if isPrime(count):
            list.append(count)
        count+=1
    return list


def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if (n%i) == 0:
            return False
    return True
