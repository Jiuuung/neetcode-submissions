class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        path=[]
        res = []
        def pick(start, remain):
            if remain==0:
                res.append(path.copy())
                return
            prev=0
            for i in range(start, len(candidates)):
                if candidates[i]==prev:
                    continue
                if candidates[i]>remain:
                    break
                path.append(candidates[i])
                pick(i+1, remain-candidates[i])
                path.pop()
                prev= candidates[i]
            return
        pick(0,target)
        return res
