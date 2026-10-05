class TrieNode:
    def __init__(self):
        self.children={}
        self.is_end = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c]=TrieNode()
            node = node.children[c]
        node.is_end = True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        #dp[i] 를 s[i:]를 처리했을때의 최소 extra의 수라고 하자.
        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        n=len(s)
        dp=[0]*(n+1)
        for i in range(n-1,-1,-1 ):
            dp[i]=dp[i+1]+1
            curr = trie.root
            for j in range(i, n):
                if s[j] not in curr.children:
                    break
                curr = curr.children[s[j]]
                if curr.is_end:
                    dp[i] = min(dp[i], dp[j+1])

        return dp[0]