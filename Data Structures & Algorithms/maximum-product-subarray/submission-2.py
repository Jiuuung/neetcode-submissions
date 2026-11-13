class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 길이와 시작점 X -> 음수 가능성도 있어서 -> 그럼 음수쪽이랑 양수쪽
        # 나눠서 저장해해두면?
        cur_min=nums[0]
        cur_max=nums[0]
        max_p=nums[0]
        for i in nums[1:]:
            tmp_max= max(i, cur_max*i, cur_min*i)
            tmp_min = min(i, cur_min*i, cur_max*i)
            cur_max= tmp_max
            cur_min = tmp_min
            max_p= max(max_p, cur_max)
        return max_p