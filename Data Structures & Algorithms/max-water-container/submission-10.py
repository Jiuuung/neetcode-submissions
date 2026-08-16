class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water=0
        one=0
        two=len(heights)-1
        while one<two:
            max_water=max(max_water,min(heights[one], heights[two])*(two-one))
            if heights[one]>heights[two]:
                two-=1
            elif heights[one]<heights[two]:
                one+=1
            else:
                while one<two and heights[one]==heights[two]:
                    max_water=max(max_water,min(heights[one], heights[two])*(two-one))
                    if heights[one+1] <heights[two-1]:
                        two-=1
                    elif heights[one+1]>heights[two-1]:
                        one+=1
                    else:
                        one+=1
                        two-=1    
            
        return max_water