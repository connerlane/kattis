import listgame2
import approach2
i = 2
while True:
	lg2 = listgame2.solve(i)
	a2 = approach2.solve(i)
	if lg2 != a2:
		with open("diff.txt", "a") as fh:
			fh.write("for input: " + str(i))
			fh.write("\nconner_michael: " + str(lg2))
			fh.write("\ngavin: " + str(lg2) + "\n\n")
			i += 1
		
	else:
		i += 1
		print(i)