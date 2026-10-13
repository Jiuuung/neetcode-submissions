class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def pick(cur,open_count, close_count):
            if open_count==n and close_count==n:
                res.append(cur)
                return
            if open_count<n:
                pick(cur+"(", open_count+1, close_count)
            if close_count<n and close_count<open_count:
                pick(cur+")", open_count, close_count+1)
            return
        pick("",0,0)
        return res

