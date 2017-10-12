def encrypt(string):
    for x in range(0, len(string)):
        if string[x] == " ":
            string[x] = 0
        else:
            string[x] = ord(string[x]) - 96
    for y in range(1, len(string)):
        string[y] += string[y - 1]
    for z in range(0, len(string)):
        string[z] = string[z] % 27 + 96
        if string[z] == 96:
            string[z] = 32
    string = [chr(q) for q in string]
    return "".join(string)
    # print("".join([chr(q) for q in string]))


def decrypt(string):
    string = [ord(e) - 96 for e in string]
    for z in range(0, len(string)):
        if string[z] == -64:
            string[z] = 0
    newlist = [string[0]]
    for x in range(1, len(string)):
        factor = 0
        while (string[x] + factor) - (string[x - 1]) < 0:
            factor += 27
        newlist.append((string[x] + factor) - (string[x - 1]))
    for z in range(0, len(newlist)):
        newlist[z] = newlist[z] + 96
        if newlist[z] == 96:
            newlist[z] = 32
    newlist = [chr(q) for q in newlist]
    return "".join(newlist)



cases = int(input())
for i in range(cases):
    line = list(input())
    t = line[0]
    del line[0]
    del line[0]
    if t == "e":
        print(encrypt(line))
    elif t == "d":
        print(decrypt(line))