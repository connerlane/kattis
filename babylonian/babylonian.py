import math

lines = eval(input())
for i in range(0, lines):
    number_arr = input().split(',')
    for j in range(0, len(number_arr)):
        if not number_arr[j]:
            number_arr[j] = '0'
    number_arr = [eval(i) for i in number_arr]
    decimal = 0
    power = 0
    while number_arr:
        n = number_arr.pop()
        decimal += (n * math.pow(60, power))
        power += 1

    print(int(decimal))
