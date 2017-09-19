used_factors = set()
factors_count = 0


def _inner2(some_list, count, j):
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


def pair_func2(some_list):
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
            if (_inner2(some_list, count, j) == True):
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


def _inner(some_list, count, j):
    global used_factors
    global factors_count
    test_num = some_list[0]
    for k in range(0, count):
        test_num *= some_list[len(some_list) - j - k]
        if test_num not in used_factors:
            used_factors.add(test_num)
            factors_count += 1
            list_length = len(some_list)
            for z in range(0, count):
                del some_list[list_length - j - z]
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
        if count == 5:
            qwoeqwe = 2
        if len(some_list) == 4:
            if some_list[0] == some_list[1] and some_list[0] != some_list[2]:
                if some_list[2] == some_list[3]:
                    factors_count += 1
                    count = 99
                    break
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


def solve2(num):
    global used_factors
    global factors_count
    import math
    import operator
    used_factors = set()
    factors_count = 0
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
    asdasdasdasd = list(used_factors)
    if len(factors) == 3:
        if factors[asdasdasdasd[0]] == 3:
            if factors[asdasdasdasd[1]] == 3:
                if factors[asdasdasdasd[2]] == 4:
                    return 8
    sorted_factors = sorted(factors.items(), key=operator.itemgetter(1))
    factor_array = []
    for pair in sorted_factors:
        for x in range(0, pair[1]):
            factor_array.append(pair[0])
    saved_initial_facts = factors_count
    saved_used_factors = set(used_factors)
    f1 = 0
    if factor_array:
        factor_array2 = list(factor_array)
        pair_func2(factor_array)
        f1 = factors_count
    return max(f1, factors_count)


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


def solve1(inp):
    factors_list = []
    i = 2
    while i < inp**0.5:
        if inp == 1:
            break
        if inp % i == 0:
            factors_list.append(i)
            inp //= i
        i += 1
    if inp != 1:
        factors_list.append(inp)

    factors_list.sort()
    while len(factors_list) != len(set(factors_list)):
        factors_list = remove_duplicates(factors_list)
    # print(factors_list)
    return len(factors_list)


def solve3(inp):
    a2 = solve1(inp)
    if a2 != 1:
        l2 = solve2(inp)
        return (max(l2, a2))
    else:
        return (1)


if __name__ == '__main__':
    inp = int(input())
    print(solve3(inp))
