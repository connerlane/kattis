from random import shuffle
import time

def _inner(some_list, count, j,
           used_factors, array_stack, checked_at_level):
    test_num = some_list[0]
    for k in range(0, count):
        test_num *= some_list[j + k]
    if test_num not in used_factors and test_num not in checked_at_level:
        checked_at_level.append(test_num)
        array_stack.append(list(some_list))
        for z in range(0, count):
            del some_list[j + k - z]
        del some_list[0]
        return test_num
    return None

def divide_multiset(multiset):
    shuffle(multiset)
    most_factors_so_far = []
    
    # Declare stacks needed
    count_stack = []
    array_stack = []
    factors_stack = []
    factors_checked_at_this_level_stack = []
    current_used_factors = []
    factors_checked_at_this_level = []
    count = 1

    # Remove one of each type and add to current_used_factors
    m_length = len(multiset)
    for i in range(1, m_length + 1):
        number = multiset[m_length - i]
        if number not in current_used_factors:
            current_used_factors.append(number)
            multiset.remove(number)

    # Short circuit if only one of each type of factor
    if not multiset:
        return current_used_factors

    # Otherwise, add starting values to stacks
    factors_stack.append(list(current_used_factors))
    factors_checked_at_this_level_stack.append(list(current_used_factors))
    count_stack.append(count)
    array_stack.append(list(multiset))
    most_factors_so_far = list(current_used_factors)

    # Begin loop

    while factors_stack:
        cur_type = multiset[0]
        while count < len(multiset):
            if multiset[0] != cur_type:
                cur_type = multiset[0]
                count = 1
            for j in range(1, len(multiset) - count + 1):
                possible_factor = _inner(multiset, count, j,
                          current_used_factors,
                          array_stack, factors_checked_at_this_level)
                if possible_factor:
                    factors_stack.append(list(current_used_factors))
                    current_used_factors.append(possible_factor)
                    count_stack.append(count)
                    factors_checked_at_this_level_stack.append(list(factors_checked_at_this_level))
                    factors_checked_at_this_level = []
                    if len(current_used_factors) >= len(most_factors_so_far):
                        most_factors_so_far = current_used_factors
                    break
                elif j == len(multiset) - count:
                    count += 1


        current_used_factors = factors_stack.pop()
        count = count_stack.pop()
        multiset = array_stack.pop()
        factors_checked_at_this_level = factors_checked_at_this_level_stack.pop()
    # print(most_factors_so_far)
    return most_factors_so_far


def solve(num):
    from math import sqrt
    import operator
    prime_factors = []
    i = 2
    while i <= sqrt(num):
        if num % i == 0:
            prime_factors.append(i)
            num //= i
            i = 2
            continue
        i += 1
    prime_factors.append(num)
    print(prime_factors)
    a_run = len(divide_multiset(list(prime_factors)))
    b_run = len(divide_multiset(prime_factors))
    return max(a_run, b_run)

if __name__ == '__main__':
    input_number = int(input())
    start_time = time.time()
    print(solve(input_number))
    finish_time = time.time()
    print(finish_time - start_time)
