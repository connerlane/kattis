x = int(raw_input())
result = []
i = 2
while i <= x:
    if x % i == 0:
        result.append(i)
        x = x / i
    i = i + 1
print len(result), result
