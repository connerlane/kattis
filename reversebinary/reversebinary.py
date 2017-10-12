import math
num = int(input())
b = bin(num)
s = str(b)
s = s[2:]
lis = [int(i) for i in list(s)]
lis.reverse()
num = 0
power = 0
while lis:
    n = lis.pop()
    num += n * math.pow(2, power)
    power += 1
print(int(num))
