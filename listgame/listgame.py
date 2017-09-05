import math
num = int(input())
primes = 1
i = 2

while (i <= math.sqrt(num)):
   if (num % i == 0):
      num //= i
      primes += 1
      i = 2
      continue
   i += 1

print(primes)