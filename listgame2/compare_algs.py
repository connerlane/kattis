import listgame2
import approach2
i = 2
while True:
	lg2 = listgame2.solve(i)
	a2 = approach2.solve(i)
	if lg2 != a2:
		print(i)
		print(lg2)
		print(a2)
		break
	else:
		i += 1
		print(i)