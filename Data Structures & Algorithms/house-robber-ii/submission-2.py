class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        elif len(nums)<=3:
            return max(nums)
        else:
            rob1=0
            rob2=0
            for i in nums[2:len(nums)-1]:
                tmp=max(rob1, rob2+i)
                rob2=rob1
                rob1=tmp
            rob3=0
            rob4=0
            for i in nums[1:]:
                tmp = max(rob3, rob4+i)
                rob4=rob3
                rob3=tmp
            return max(rob3, rob1+nums[0])

