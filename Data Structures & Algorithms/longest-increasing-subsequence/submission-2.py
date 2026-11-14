class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        brute force: 하나의 인덱스 별로 다 해보기. 인덱스 하나 고르고 그 아래로 해당 인덱스 값보다 큰 원소들로만 구성된 배열 넘기기+ 현재 길이도 
        여기서 중복은 특정 인덱스 이후부터 최대 길이 구하는 과정들이 중복될수도 있음.(시작 값에 따라 물론 다름)
        다른 방법: 뒤에서 부터 계산. dp[i]를 i에서 시작해서 제일 긴 길이로 하고 계산시 현재 인덱스 j에서의 값이랑 dp에서 그 이후부터 인덱스 값 비교하면서 j값보다 큰 인덱스 찾고 그거 +1로 하기.
        마지막에는 dp중 제일 큰 값으로 결정.
        다른 방법: dp[k]를 k+1 길이 sequence만들 수 있는 마지막 원소 중 작은걸로 유지.
        """

        dp=[nums[0]]
        for i in nums[1:]:
            if i>dp[-1]:
                dp.append(i)
            else:
                for j in range(0, len(dp)):
                    if i<dp[j]:
                        dp[j]=i
                        break
                    elif i==dp[j]:
                        break
        return len(dp)
        



        