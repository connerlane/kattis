import time
import random

def rabinMiller(num):
    # Returns True if num is a prime number.

    s = num - 1
    t = 0
    while s % 2 == 0:
        # keep halving s while it is even (and use t
        # to count how many times we halve s)
        s = s // 2
        t += 1

    for trials in range(5): # try to falsify num's primality 5 times
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1: # this test does not apply if v is 1.
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
    return True


def is_prime(num):
    # Return True if num is a prime number. This function does a quicker
    # prime number check before calling rabinMiller().

    if (num < 2):
        return False # 0, 1, and negative numbers are not prime

    # About 1/3 of the time we can quickly determine if num is not prime
    # by dividing by the first few dozen prime numbers. This is quicker
    # than rabinMiller(), but unlike rabinMiller() is not guaranteed to
    # prove that a number is prime.
    lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

    if num in lowPrimes:
        return True

    # See if any of the low prime numbers can divide num
    for prime in lowPrimes:
        if (num % prime == 0):
            return False

    # If all else fails, call rabinMiller() to determine if num is a prime.
    return rabinMiller(num)


def remove_duplicates(l):
    i = 0
    for j in range(1, len(l)):
        if l[i] == l[j]:
            k = l[i] * l[len(l) - 1]
            del l[j]
            del l[i]
            l.append(k)
            break
        i += 1
    l.sort()
    return l

def backtrack(factors_list, number):
    cur_highest = list(factors_list)
    number_backup = number
    list_copy = list(factors_list)
    for x in range(1, len(factors_list) + 1):
        for y in range(1, x):
            list_copy.pop()
        skip = list_copy.pop() + 1
        for z in list_copy:
            number //= z
        while skip <= number**0.5:
            if number % skip == 0:
                list_copy.append(skip)
                number //= skip
            skip += 1
        if number != 1:
            list_copy.append(number)
        remove_duplicates(list_copy)
        if len(list_copy) > len(cur_highest):
            return list_copy
        list_copy = list(factors_list)
        number = number_backup
    return cur_highest

def solve(inp):
    if inp == 1:
        return 1
    factors_list = []
    i = 2
    number = inp
    flag = True
    limit = inp**0.5
    while i <= limit:
        if i > 250000:
            return len(factors_list) + 2
        if flag:
            if is_prime(inp):
                return len(factors_list) + 1
            for n in factors_list:
                if inp % n == 0:
                    if is_prime(inp // n):
                        return len(factors_list) + 1
            flag = False
        if inp % i == 0:
            flag = True
            factors_list.append(i)
            inp //= i
            limit = inp**0.5
        i += 1
    if inp != 1:
        factors_list.append(inp)
    factors_list.sort()
    if len(factors_list) != len(set(factors_list)):
        factors_list = remove_duplicates(factors_list)
    factors_list = backtrack(factors_list, number)
    # print(factors_list)
    return len(factors_list)

if __name__ == '__main__':

    inp = int(input())
    start_time = time.time()
    print(solve(inp))
    # print(time.time() - start_time)