import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums)-k
        left =0 #pivot> 보다 1개 더 간것
        right = len(nums)-1 # pivot< 보다 1개 더 작은것
    
        while left<=right:
            pivot = nums[random.randint(left, right)]
            
            lt= left
            i = left
            gt = right

            while i<=gt:
                if nums[i]<pivot:
                    nums[i], nums[lt] = nums[lt], nums[i]
                    lt+=1
                    i+=1
                elif nums[i]==pivot:
                    i+=1
                else:
                    nums[i], nums[gt]=nums[gt], nums[i]
                    gt-=1
            
            if target<lt:
                right = lt-1
            elif target>gt:
                left = gt+1
            else:
                return pivot
            
