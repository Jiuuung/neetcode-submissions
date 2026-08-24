class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)

        l,r = 0, length-1
        while l<=r:
            mid = int((r-l)/2)+l
            if target==nums[mid]:
                return mid
            elif target>nums[mid]:
                l=mid+1
            else:
                r=mid-1
        return -1
