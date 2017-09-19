from math import sqrt

fibs = []


def gen_fib():
    fibs.append("0")
    fibs.append("1")
    for i in range(50):
        fibs.append(fibs[len(fibs) - 1] + fibs[len(fibs) - 2])
        fibs.pop(0)
    return fibs[len(fibs) - 1]


print(gen_fib())
