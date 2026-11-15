class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        전체 합 /2 한게 subset1에 들어가야 하는 값의 합임.
        그러면 dfs 마냥 각 원소 넣을지 말지로 분기해서 전체 다 계산하고 하나라도 성립하는게 나오면 true가 되는것임.
        dp[i]를 i라는 숫자를 만들 수 있는지로 본다면? 그럼 새로운 인덱스마다 모든 dp를 순회해야 하기에 묹가 될 수 있다.
   """
        target = sum(nums)
        if target%2==1:
            return False
        else:
            target=target//2
            dp=[False]*(target+1)
            dp[0]=True
            for num in nums:
                for i in range(target-1, -1, -1):
                    if dp[i]==True and (i+num)<=target:
                        dp[i+num]=True
            return dp[-1]
