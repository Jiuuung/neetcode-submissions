class Solution:
    def countSubstrings(self, s: str) -> int:
        dp=[[False]*len(s) for _ in range(len(s))]
        count=0
        for i in range(len(s)):
            dp[i][i]=True
            count+=1
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                dp[i][i+1]=True
                count+=1
        for size in range(3,len(s)+1):
            for i in range(len(s)-size+1):
                j=i+size-1
                if (s[i]==s[j]) and dp[i+1][j-1]:
                    dp[i][j]=True
                    count+=1
        return count
