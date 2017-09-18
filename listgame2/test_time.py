import time
import approach2



for x in range(10**7, 10**15):
	print(x)
	s_time = time.time()
	approach2.solve(x)
	t = time.time() - s_time
	if t > 2:
		with open("timeout.txt", "a") as fh:
			fh.write("for input: " + str(x) + "\n")
			fh.write("took: " + t + " seconds\n\n")
	