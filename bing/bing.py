class tree_node:

    def __init__(self, character, parent, end_of_word=False):
        self.character = character
        self.parent = parent
        self.end_of_word = False
        self.children = dict()

    def add_child(self, child):
        self.children[child] = None

    def __str__(self):
        return(self.character + " " + str(self.parent))

    def __hash__(self):
        return hash((self.character))

class prefix_tree:
    def __init__(self):
        self.tree = tree_node("", None)

    def get_all_children(self, node, all_children):
        for k in node.children:
            c = node.children[k]
            if c.end_of_word:
                d = c
                word = []
                while d.parent:
                    word.append(d.character)
                    d = d.parent
                word_string = "".join(reversed(word))
                all_children.append(word_string)
            self.get_all_children(c, all_children)
        return all_children





    def contains(self, word):
        word_list = list(word)
        level = self.tree
        x = 0
        while x < len(word_list):
            if word_list[x] not in level.children:
                for i in range(x, len(word_list)):
                    level.children[word_list[i]] = tree_node(word_list[i], level)
                    level = level.children[word_list[i]]
                level.end_of_word = True
                return []
            level = level.children[word_list[x]]
            x += 1
        level_pointer = level
        child_words = self.get_all_children(level, [])
        level_pointer.end_of_word = True
        return child_words
            


if __name__ == "__main__":
    number_of_lines = int(input())
    
    t = prefix_tree()
    for x in range(0, number_of_lines):
        if x == 9:
            q = 2
        word = input()
        print(len(t.contains(word)))
    # print(t.contains(""))
