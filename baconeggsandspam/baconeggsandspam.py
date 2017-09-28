
while True:
	number = int(input())
	if number == 0:
		break
	menu_items = dict()
	for x in range(number):
		order = input().split()
		for y in range(1, len(order)):
			if order[y] not in menu_items:
				menu_items[order[y]] = [order[0]]
			else:
				menu_items[order[y]].append(order[0])
	for item in sorted(menu_items):
		print(item, end=" ")
		print(" ".join(sorted(menu_items[item])))
	print()
