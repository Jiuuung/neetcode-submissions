class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[[]]
        prev_idx=0
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                start = prev_idx
            else:
                start = 0
            end=len(res)
            for j in range(start,end):
                tmp = res[j].copy()
                tmp.append(nums[i])
                res.append(tmp)
            prev_idx=end
        return res