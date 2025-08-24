import time


def main():
    nth = input("Input: ")
    start_time = time.time()
    prime_counter(nth)
    elapsed_time = time.time() - start_time
    print(elapsed_time)

def prime_counter(n):
    number_of_primes_checked = 2
    x = 4
    int_n = int(n)
    primes_list = [2, 3]
    while len(primes_list) < int_n:
        if prime_checker(x):
            number_of_primes_checked += 1
            primes_list.append(x)
            x += 1
        else:
            x += 1
    print(primes_list[-1])


def prime_checker(n):
    if n % 2 != 0 and n % 3 != 0:
        for i in range(2, int(n**0.5)+1):
            if int(n) % i == 0:
                return False
            else:
                continue
        return True
    else:
        return False

main()
