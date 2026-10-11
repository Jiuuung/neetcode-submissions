class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        index = 0
        subsets = []
        def pick(subset :List[int], index):
            if index ==len(nums):
                subsets.append(subset)
                return
            pick(subset, index+1)
            pick(subset + [nums[index]], index+1)
        subset = []
        pick(subset, index)
        return subsets


