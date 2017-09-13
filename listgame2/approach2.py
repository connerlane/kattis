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

def solve(inp):
    factors_list = []
    i = 2
    while i < inp:
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

    return len(factors_list)

if __name__ == '__main__':
    
    inp = int(input())
    print(solve(inp))