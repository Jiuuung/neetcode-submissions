class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        one=0
        two=len(numbers)-1
        while one<two:
            if (target-numbers[one])>numbers[two]:
                one+=1
            elif (target-numbers[one])<numbers[two]:
                two-=1
            else:
                return [one+1,two+1]