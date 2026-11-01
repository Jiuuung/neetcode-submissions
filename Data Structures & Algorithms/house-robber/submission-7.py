class Solution:
    def rob(self, nums: List[int]) -> int:
        a,b=0,0
        for i in nums:
            tmp = max(i+a,b)
            a=b
            b=tmp
        return b