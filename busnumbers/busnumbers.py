trash = input()
stops = [int(i) for i in input().split()]
stops.sort()
sequential = 1
shortened = dict()
i = 1
while i < len(stops):
    if stops[i] == stops[i - 1] + 1:
        sequential += 1
        if sequential >= 3:
            shortened[stops[i - sequential + 1]] = stops[i]
    else:
        sequential = 1
    i += 1
outputstring = ""

for key, value in shortened.items():
    arr = list(range(key, value + 1))
    for a in arr:
        stops.remove(a)


shortened_keys = sorted(shortened)
# print(shortened_keys)
# print(stops)

while shortened_keys or stops:
    if stops and shortened_keys:
        if stops[0] < shortened_keys[0]:
            outputstring += str(stops[0]) + " "
            del stops[0]
        else:
            outputstring += str(shortened_keys[0]) + "-" + str(shortened[shortened_keys[0]]) + " "
            del shortened_keys[0]
    elif stops:
        outputstring += str(stops[0]) + " "
        del stops[0]
    else:
        outputstring += str(shortened_keys[0]) + "-" + str(shortened[shortened_keys[0]]) + " "
        del shortened_keys[0]
print(outputstring)

    

