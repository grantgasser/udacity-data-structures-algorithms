class Node:
    """
    Node class
    """
    def __init__(self, points=0):
        self.points = points
        self.children = {}  # char: Node


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word, points):
        """
        Inserts a word into the trie
        """
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Node(points=points)
            else:
                if points > curr.children[ch].points:
                    curr.children[ch].points = points
                # else:
                #     curr.children[ch].points += points
            curr = curr.children[ch]
        curr.children['*'] = True

    def search(self, word):
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]

        if '*' in curr.children:
            return True
        else:
            return False

    def autocomplete_scores(self, query):
        curr = self.root

        for ch in query:
            if ch not in curr.children:
                return 0

            curr = curr.children[ch]

        return curr.points


def main():
    trie = Trie()

    # trie.insert('hi')
    # trie.insert('hello')
    #
    # print(trie.search('hi'))
    # print(trie.search('hello'))
    # print(trie.search('hel'))
    # print(trie.search('hey'))

    titles = ['ANIMALS', 'DOG FACTS']
    bodies = ['ANT ANTELOPE CAMEL CAT DOG', 'FURRY FURRY LOYAL']

    # insert titles
    for title in titles:
        words = title.split()

        for word in words:
            trie.insert(word, 10)


    # insert bodies
    for body in bodies:
        words = body.split()

        for word in words:
            trie.insert(word, 1)

    print(trie.root.children['A'].children['N'].children['I'].points)

    print("'AN' score:", trie.autocomplete_scores('AN'))  # 10
    print("'CAT' score:", trie.autocomplete_scores('CAT'))  # 1
    print("'DOG' score:", trie.autocomplete_scores('DOG'))  # 11
    print("'FURRY' score:", trie.autocomplete_scores('FURRY'))  # 2
    print("'DO' score:", trie.autocomplete_scores('DO'))  # 11
    print("'FUR' score:", trie.autocomplete_scores('FUR'))  # 2
    print("'ELEPH' score:", trie.autocomplete_scores('ELEPH'))  # 0


main()





