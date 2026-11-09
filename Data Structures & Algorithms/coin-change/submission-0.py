class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF=float('inf')
        dp=[INF]*(amount+1)
        dp[0]=0
        for i in range(1,amount+1):
            for k in coins:
                if i>=k and (dp[i-k]!=INF or i==k):
                    dp[i]= min(dp[i-k]+1, dp[i])
        return dp[-1] if dp[-1]!=INF else -1