class Solution:
    def longestPalindrome(self, s: str) -> str:
        long=""
        length=0
        dp=[[-1]*len(s) for _ in s]
        for i in range(len(s)):
            dp[i][i]=True
            long=s[i]
            length=1
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                dp[i][i+1]=True
                long=s[i:i+2]
                length=2
        for size in range(3,len(s)+1):
            for i in range(len(s)-size+1):
                j=i+size-1
                if dp[i][j]==-1:
                    dp[i][j]=((s[i]==s[j]) and dp[i+1][j-1])
                    if dp[i][j]==True:
                        if length<j-i+1:
                            long=s[i:j+1]
                            length=j-i+1
        return long