class Solution:

    def partition(self, s: str) -> List[List[str]]:
        s=s+"0"
        res = []

        path =[]
        def is_palindrome(start, end):
            for i in range((end-start+1)//2) or [0]:
                if s[start+i]!=s[end-i]:
                    return False
            return True

        def dfs(start):
            if start==len(s)-1:
                res.append(path.copy())
                return
            for i in range(start, len(s)):
                if is_palindrome(start, i):
                    path.append(s[start:i+1])
                    dfs(i+1)
                    path.pop()
            return
        dfs(0)
        return res
