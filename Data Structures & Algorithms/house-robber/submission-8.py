class Solution:
    def rob(self, nums: List[int]) -> int:
        #a는 i-2 까지의 best, b는 i-1까지의 best
        a,b=0,0
        for i in nums:
            tmp = max(i+a,b)
            a=b
            b=tmp
        return b