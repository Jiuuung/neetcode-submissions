class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        subsets=[]
        def pick(comb, index, subset):
            if comb==0:
                subsets.append(subset)
                return
            for ind, num in enumerate(nums[index:], start=index):
                if comb-num>=0:
                    pick(comb-num, ind, subset+[num])
        pick(target, 0, [])
        return subsets