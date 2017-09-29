import sys
inp = sys.stdin
inp = inp.read()
inp = inp.split()

while inp:
    a = int(inp[0])
    b = int(inp[1])
    del inp[0]
    del inp[0]
    print(abs(a - b))
