class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp=[]
        for i in range(len(s)):
            if s[:i+1] in wordDict:
                dp.append(i)
                continue
            else:
                for j in dp:
                    if s[j+1:i+1] in wordDict:
                        dp.append(i)
                        break
        if not dp or dp[-1]!=(len(s)-1):
            return False
        return True
             

            