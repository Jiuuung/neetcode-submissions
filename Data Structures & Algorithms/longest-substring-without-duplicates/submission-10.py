class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        length = 1
        s=list(s)
        if not s:
            return 0
        substring_dict={s[0]:0}
        for i in range(1,len(s)):
            if s[i] in substring_dict:
                length = max(length, r-l+1)
                tmp=l
                l=substring_dict[s[i]]+1
                for k in s[tmp:l]:
                    del substring_dict[k]
            r+=1
            substring_dict[s[i]]=i
        length = max(length, r-l+1)
        return length
