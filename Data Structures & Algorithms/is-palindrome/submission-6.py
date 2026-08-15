class Solution:
    def isPalindrome(self, s: str) -> bool:
        length=len(s)
        one=0
        two=length-1
        s=s.lower()
        s=list(s)
        while one<two:
            while two>=1 and (not s[two].isalnum()):
                two-=1
            
            while one<length-1 and (not s[one].isalnum()):
                one+=1
            if one>=two:
                return True
            if s[one]!=s[two] :
                return False
            else:
                one+=1
                two-=1
        return True
