import math
import time
num = int(input())
start_time = time.time()
factors_count = 1
i = 2
while i <= math.sqrt(num):
    if num % i == 0:
        num //= i
        factors_count += 1
        i = 2
        continue
    i += 1
print(factors_count)
finish_time = time.time()
print(finish_time - start_time)
