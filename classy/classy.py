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
                self_rank = self.rank[a - x]
            else:
                self_rank = "middle"
            if x <= b:
                other_rank = other.rank[b - x]
            else:
                other_rank = "middle"

            if self_rank == "upper" or other_rank == "upper":
                if self_rank != "upper":
                    return True
                elif other_rank != "upper":
                    return False
                else:
                    continue
            if self_rank == "middle" or other_rank == "middle":
                if self_rank != "middle":
                    return True
                elif other_rank != "middle":
                    return False
                else:
                    continue
        if self.name < other.name:
            return False
        return True


if __name__ == "__main__":
    cases = int(input())
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
