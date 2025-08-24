def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b)//gcd(a, b) 

def is_prime(n):
    small_primes = {2, 3}
    if n <= 1:
        return False
    elif n == 2 or n == 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        for i in range(5, int(n**0.5)+1, 6):
            if n % i == 0:
                return False
            if n % (i + 2) == 0:
                return False
        return True
    
    
def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = 0
    for p in range(2, int(n ** 0.5) + 1):
        if is_prime[p]:
            for multiple in range(p*p, n+1, p):
                is_prime[multiple] = False
    primes = []
    for prime, prime_status in enumerate(is_prime):
        if prime_status:
            primes.append(prime)
    return primes

def modinv(a, m):
    ...

def is_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 == 0 and year % 400 != 0:
        return False
    else:
        return True

def fibonacci(n):
    ...

def matrix_mult(matrix):
    ...

def matrix_pow(matrix):
    ...

def matrix_add(matrix):
    ...

def BoyerMoore_Majority_Vote(arr):
    candidate = None
    count = 0
    for i in arr:
        if count == 0:
            candidate = i
        elif i == candidate:
            count += 1
        else:
            count -= 1
    count = 0
    for i in arr:
        if i == candidate:
            count += 1
    if count > len(arr)//2:
        return candidate
    else:
        return None

def highest_frequency(arr):
    frequency_table = {}
    for i in arr:
        frequency_table[i] = frequency_table.get(i, 0) + 1
    highest_frequency = max(frequency_table.values())
    highest_frequencies = {i for i in frequency_table if frequency_table[i] == highest_frequency}
    if len(highest_frequencies) == 1:
        return next(iter(highest_frequencies))
    else:
        return list(highest_frequencies)



def duplicate(arr):
    seen = set()
    duplicates = set()
    for i in arr:
        if i in seen:
            duplicates.add(i)
        else:
            seen.add(i)
    return list(duplicates)

def validateLength(ip, lower=0, upper=float("inf")):
    """
    validateLength(ip, lower=0, upper=float("inf"))
    """
    return lower <= len(ip) <= upper



print(sieve_of_eratosthenes(1000))