import listgame2


times_taken_to_fail = []
for q in range(0, 8):
    x = 7
    i = 0
    while x == 7:
        x = listgame2.solve(165888)
        i += 1
    times_taken_to_fail.append(i)
times_taken_to_fail.sort()
print(times_taken_to_fail)
print(sum(times_taken_to_fail) / float(len(times_taken_to_fail)))
