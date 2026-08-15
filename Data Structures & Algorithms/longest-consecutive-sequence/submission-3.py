class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        longest=1
        nums.sort()
        prev=nums[0]
        length=1
        for num in nums[1:]:
            if num==prev+1:
                length+=1
                if length>longest:
                    longest=length
            elif num==prev:
                continue
            else:
                length=1
            prev=num
        return longest