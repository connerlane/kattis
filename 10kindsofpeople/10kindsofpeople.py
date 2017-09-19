import sys
sys.setrecursionlimit(10000)

r, c = [eval(i) for i in input().split()]
matrix = [[eval(i) for i in list(input())] for y in range(r)]
num_queries = eval(input())


class Point:
    def __init__(self, r, c):
        self.r = r
        self.c = c

    def __eq__(self, other):
        return (self.r == other.r and self.c == other.c)

    def __hash__(self):
        return hash((self.r, self.c))


def in_range(point):
    if (0 <= point.r <= r - 1) and (0 <=
                                    point.c <= c - 1):
        return True
    return False


def _do_dfs(mat, start, goal, valid_type, visited, path):
    if (start == goal):
        return True
    if (len(path) == 0):
        return False
    adjacent_list = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for pair in adjacent_list:
        next_point = Point(start.r + pair[0], start.c + pair[1])
        if (in_range(next_point) and mat[next_point.r][next_point.c] == valid_type
                and next_point not in visited):
            visited.add(next_point)
            path.append(next_point)
            return _do_dfs(mat, next_point, goal, valid_type, visited, path)
    old = path.pop()
    return _do_dfs(mat, old, goal, valid_type, visited, path)


def dfs(mat, start, goal, valid_type):
    visited = set()
    visited.add(start)
    path = []
    path.append(start)
    return _do_dfs(mat, start, goal, valid_type, visited, path)


for j in range(num_queries):
    r1, c1, r2, c2 = [eval(i) for i in input().split()]
    start_type = matrix[r1 - 1][c1 - 1]
    start = Point(r1 - 1, c1 - 1)
    goal = Point(r2 - 1, c2 - 1)
    found = dfs(matrix, start, goal, start_type)
    if found:
        if (start_type == 0):
            print("binary")
        elif (start_type == 1):
            print("decimal")
    else:
        print("neither")
