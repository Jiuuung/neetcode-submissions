class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        result=[0]*len(temperatures)
        for idx, temp in enumerate(temperatures):
            while stack and temp>stack[-1][0]:
                pre_val, ori_idx=stack.pop()
                result[ori_idx]=idx-ori_idx
            stack.append((temp,idx))
        return result