class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1=list(s1)
        s2=list(s2)
        s1_length=len(s1)
        s1_dict = dict()
        for s in s1:
            if not (s in s1_dict):
                s1_dict[s]=1
            else:
                s1_dict[s]+=1
        s2_length=len(s2)
        l=0
        while l<(s2_length):
            if s2[l] in s1_dict:
                r=l
                tmp_dict=s1_dict.copy()
                while r<s2_length:
                    if (not (s2[r] in tmp_dict)) or tmp_dict[s2[r]]==0:
                        break
                    else:
                        if r-l+1==s1_length:
                            return True
                        tmp_dict[s2[r]]-=1
                    r+=1
            l+=1
        return False