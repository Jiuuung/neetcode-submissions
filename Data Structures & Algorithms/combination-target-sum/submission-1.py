class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        subsets=[]

        path = []
        def pick(comb, index):
            if comb==0:
                subsets.append(path.copy())
                return
            for i in range(index, len(nums)):
                num = nums[i]
                if comb-num>=0:
                    path.append(num)
                    pick(comb-num, i)
                    path.pop()
        pick(target, 0)
        return subsets