cases = int(input())


class Person:
    def __init__(self, name, rank):
        self.name = name[:-1]
        self.rank = rank.split("-")

    def __lt__(self, other):
        a = len(self.rank)
        b = len(other.rank)
        c = max(a, b)
        for x in range(1, c + 1):
            if x <= a:
                sr = self.rank[a - x]
            else:
                sr = "middle"
            if x <= b:
                tr = other.rank[b - x]
            else:
                tr = "middle"

            if sr == "upper" or tr == "upper":
                if sr != "upper":
                    return True
                elif tr != "upper":
                    return False
                else:
                    continue
            if sr == "middle" or tr == "middle":
                if sr != "middle":
                    return True
                elif tr != "middle":
                    return False
                else:
                    continue
        if self.name < other.name:
            return False
        return True


for i in range(cases):
    people = int(input())
    people_list = []
    for j in range(people):
        inp = input().split()
        people_list.append(Person(inp[0], inp[1]))
    people_list.sort(reverse=True)
    for p in people_list:
        print(p.name)
    print("=" * 30)
