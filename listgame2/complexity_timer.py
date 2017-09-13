import listgame2
import time
with open("listgame2.csv", "w") as fh:
	x = 2
	while x < 50:
		t = time.time()
		listgame2.solve(2**x)
		s = time.time()
		fh.write(str(eval("2**" + str(x))) + ", " + str(s - t) + "\n")
		x += 1

# import approach2
# import time
# with open("approach2.csv", "w") as fh:
# 	x = 2
# 	while x < 30:
# 		t = time.time()
# 		approach2.solve(2**x)
# 		s = time.time()
# 		fh.write("2^" + str(x) + ", " + str(s - t) + "\n")
# 		x += 1