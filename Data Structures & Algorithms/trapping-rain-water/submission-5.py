class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        res=0
        l, left_max=0, height[0]
        r, right_max= len(height)-1, height[-1]
        while l<r:
            if left_max<right_max:
                l+=1
                left_max= max(left_max, height[l])
                res+=left_max-height[l]
            else:
                r-=1
                right_max= max(right_max, height[r])
                res+=right_max-height[r]
        return res