class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict={}
        res=[]
        if len(digits)==0:
            return res
        for i in range(2,7):
            if i==7:
                continue
            dict[i]=[chr(90+3*i+1),chr(90+3*i+2),chr(90+3*i+3)]
        dict[7]=["p","q","r","s"]
        dict[8]=["t","u","v"]
        dict[9]=["w","x","y","z"]
        def dfs(ind, comb):
            if ind==len(digits):
                res.append(comb)
                return
            for k in dict[int(digits[ind])]:
                dfs(ind+1, comb+k)
            return
        dfs(0,"")
        return res