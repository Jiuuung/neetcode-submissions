class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        re=set()
        l=len(nums)
        nums.sort()
        for one in range(l-2):
            two=one+1
            three=l-1
            target=-nums[one]
            while two<three:
                if (nums[two]+nums[three])<target:
                    two+=1
                elif (nums[two]+nums[three])>target:
                    three-=1
                else:
                    re.add((nums[one],nums[two], nums[three]))
                    two+=1
        return [list(i) for i in re]