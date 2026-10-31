class Solution:
    def climbStairs(self, n: int) -> int:
        dp =[-1]*n
        dp[0]=1
        if n>=2:
            dp[1]=2
            if n>=3:
                for i in range(2,n):
                    dp[i]=dp[i-1]+dp[i-2]
        return dp[n-1]
