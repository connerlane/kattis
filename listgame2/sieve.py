primes = set()


def sieve2(n):
    loops = 0
    numbers = range(0, n)
    for prime in numbers:
        if prime < 2:
            continue
        elif prime > n ** 0.5:
            break
        for i in range(prime ** 2, n, prime):
            numbers[i] = 0
    return [x for x in numbers if x > 1]


primes = set(sieve2(100000000))
print(primes)
