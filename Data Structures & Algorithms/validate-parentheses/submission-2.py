class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for bracket in s:
            if bracket == ")":
                if len(stack)==0:
                    return False
                compare=stack.pop()
                if compare!="(":
                    return False
            elif bracket == "}":
                if len(stack)==0:
                    return False
                compare=stack.pop()
                if compare!="{":
                    return False
            elif bracket == "]":
                if len(stack)==0:
                    return False
                compare=stack.pop()
                if compare!="[":
                    return False
            else:
                stack.append(bracket)
        if len(stack)==0:
            return True
        return False