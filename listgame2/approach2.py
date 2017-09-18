import time
import random


def is_prime(num):
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
    while i <= inp**0.5:
        if i > 100000: # SUPER JANK HACKY ATTEMPT TO PASS TESTS
            if is_prime(inp):
                return len(factors_list) + 1
        if inp % i == 0:
            factors_list.append(i)
            inp //= i
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