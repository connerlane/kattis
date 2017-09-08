import math

lines = eval(input())
for i in range(0, lines):
    number_arr = input().split(',')
    decimal = 0
    power = 0
    while number_arr:
        n = number_arr.pop()
        if n:
            decimal += (eval(n) * math.pow(60, power))
            power += 1
        else:
            power += 1

    print(int(decimal))
