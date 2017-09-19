import listgame2
import dfs
import os
i = 1
while i <= 10**15:
    dfs2 = dfs.solve(i)
    gross = listgame2.solve(i)

    if dfs2 != gross:
        with open("diff.txt", "a") as fh:
            fh.write("for input: " + str(i))
            fh.write("\na2: " + str(gross))
            fh.write("\ndfs: " + str(dfs2) + "\n\n")
            i += 1
            # os.system('say "discrepancy found"')

    else:
        i += 1
        print(i)
