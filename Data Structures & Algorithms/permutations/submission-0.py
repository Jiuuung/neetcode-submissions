class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visit=[False]*len(nums)
        res=[]
        path=[]
        def pick():
            if all(visit):
                res.append(path.copy())
                return
            for i in range(len(nums)):
                if visit[i]==False:
                    visit[i]=True
                    path.append(nums[i])
                    pick()
                    visit[i]=False
                    path.pop()
            return
        pick()
        return res