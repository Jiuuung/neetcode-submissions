class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        path =[]
        def pick(start):
            if start==len(nums):
                if path not in res:
                    res.append(path.copy())
                return
            path.append(nums[start])
            pick(start+1)
            path.pop()
            pick(start+1)
            return
        pick(0)
        return res