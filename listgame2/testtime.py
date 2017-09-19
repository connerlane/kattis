import time
import listgame2

range_constant = 10**15

for x in range(0, range_constant):
    print(range_constant - x)
    s_time = time.time()
    z = listgame2.solve(range_constant - x)
    print("\t" + str(z))
    t = time.time() - s_time
    if t > 2:
        with open("timeout2.txt", "a") as fh:
            fh.write("for input: " + str(range_constant - x) + "\n")
            fh.write("took: " + str(t) + " seconds\n\n")
