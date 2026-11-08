class Solution:
    def longestPalindrome(self, s: str) -> str:
        long=""

        for i in range(0,len(s)):
            tmp=(i,i)
            left=i-1
            right=i+1
            while left>=0 and right<=len(s)-1 and s[left]==s[right]:
                tmp=(left, right)
                left-=1
                right+=1
            if tmp[1]-tmp[0]+1>len(long):
                long=s[tmp[0]:tmp[1]+1]
        for i in range(0,len(s)-1):
            if s[i]!=s[i+1]:
                continue
            tmp=(i,i+1)
            left=i-1
            right=i+2
            while left>=0 and right<=len(s)-1 and s[left]==s[right]:
                tmp=(left, right)
                left-=1
                right+=1
            if tmp[1]-tmp[0]+1>len(long):
                long=s[tmp[0]:tmp[1]+1]
        return long