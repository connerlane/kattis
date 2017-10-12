cases = int(input())

for x in range(cases):
    gnomes = [int(i) for i in input().split()]
    first = gnomes[1]
    for y in range(2, len(gnomes) - 1):
        if gnomes[y] != first + y - 1:
            print(y)
            break