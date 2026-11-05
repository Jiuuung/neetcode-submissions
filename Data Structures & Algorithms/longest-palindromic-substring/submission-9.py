class Solution:
    def longestPalindrome(self, s: str) -> str:
        long=""

        for i in range(0,len(s)):
            tmp=s[i]
            left=i-1
            right=i+1
            while left>=0 and right<=len(s)-1 and s[left]==s[right]:
                tmp=s[left]+tmp+s[right]
                left-=1
                right+=1
            if len(tmp)>len(long):
                long=tmp
        for i in range(0,len(s)-1):
            if s[i]!=s[i+1]:
                continue
            tmp=s[i:i+2]
            left=i-1
            right=i+2
            while left>=0 and right<=len(s)-1 and s[left]==s[right]:
                tmp=s[left]+tmp+s[right]
                left-=1
                right+=1
            if len(tmp)>len(long):
                long=tmp
        return long