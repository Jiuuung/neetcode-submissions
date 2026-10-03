class TrieNode:
    def __init__(self):
        self.children={}
        self.is_end =False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c]=TrieNode()
            node = node.children[c]

        node.is_end = True
    def search(self, word: str) -> bool:
        node = self.root
        def se(index, n_node):
            if index == len(word):
                return n_node.is_end
            c = word[index]
            if c != '.':
                if c not in n_node.children:
                    return False
                return se(index+1, n_node.children[c])
            for child in n_node.children.values():
                if se(index+1, child):
                    return True
            return False           
        return se(0, node)
