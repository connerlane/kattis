used_factors = set()
factors_count = 0
def _inner(some_list, count, j):
    global used_factors
    global factors_count
    test_num = some_list[0]
    for k in range(0, count):
        test_num *= some_list[j + k]
        if test_num not in used_factors:
            used_factors.add(test_num)
            factors_count += 1
            for z in range(0, count):
                del some_list[j + k - z]
            del some_list[0]
            return True
    return False

def pair_func(some_list):
    global factors_count
    global used_factors
    count = 1
    dummy = used_factors
    cur_type = some_list[0]
    while (count < len(some_list)):
        if some_list[0] != cur_type:
            cur_type = some_list[0]
            count = 1
        for j in range(1, len(some_list) - count + 1):
            if (_inner(some_list, count, j) == True):

                break
            elif j == len(some_list) - count:
                count += 1
    if some_list:
        last_fact = 1
        for unused_element in some_list:
            last_fact *= unused_element
        if last_fact not in used_factors:
            used_factors.add(last_fact)
            factors_count += 1
        else:
            sorted_factors = sorted(used_factors)
            highest_factor = sorted_factors.pop()
            used_factors.remove(highest_factor)
            used_factors.add(highest_factor * last_fact)

def solve(num):
    global used_factors
    global factors_count
    import math
    import operator
    used_factors = set()
    factors = {}
    i = 2
    while i <= math.sqrt(num):
        if num % i == 0:
            if i in factors:
                factors[i] += 1
            else:
                factors[i] = 1
            num //= i
            i = 2
            continue
        i += 1
    if num in factors:
        factors[num] += 1
    else:
        factors[num] = 1 

    for fact, amount in factors.items():
        used_factors.add(fact)
        factors[fact] -= 1
        factors_count += 1

    sorted_factors = sorted(factors.items(), key=operator.itemgetter(1), reverse=True)
    factor_array = []
    for pair in sorted_factors:
        for x in range(0, pair[1]):
            factor_array.append(pair[0])
    if factor_array:
        pair_func(factor_array)
    f = factors_count
    factors_count = 0
    print(used_factors)
    return f

if __name__ == '__main__':
    input_number = int(input())
    print(solve(input_number))
