from queue import Queue
from copy import deepcopy


class Node:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neighbors = []
        self.visited = False

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False


def assign_neighbors(nodes):
    # only assigns X as a neighbor of Y if X and Y are not farther than 1000m apart
    # (manhattan distance)
    for node in nodes:
        for other_node in nodes:
            if other_node != node:
                if (abs(node.x - other_node.x) +
                        abs(node.y - other_node.y) <= 1000):
                    node.neighbors.append(other_node)


def bfs(start_node, stores, goal_node):
    # populate every node's neighbors
    assign_neighbors([start_node] + stores + [goal_node])
    q = Queue()
    q.put(start_node)
    while q.queue:
        n = q.get()
        if n == goal_node:
            return True
        n.visited = True
        for m in n.neighbors:
            if not m.visited:
                q.put(m)
    return False


if __name__ == "__main__":
    test_cases = int(input())

    for i in range(test_cases):
        number_of_stores = int(input())
        jo_house_x, jo_house_y = [int(element) for element in input().split()]
        start_node = Node(jo_house_x, jo_house_y)
        stores = []
        for j in range(number_of_stores):
            stores.append([int(element) for element in input().split()])
        stores = [Node(element[0], element[1]) for element in stores]
        goal_x, goal_y = [int(element) for element in input().split()]
        goal_node = Node(goal_x, goal_y)

        if bfs(start_node, stores, goal_node):
            print("happy")
        else:
            print("sad")
