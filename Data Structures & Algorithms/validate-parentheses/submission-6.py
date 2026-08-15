class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closeToOpen={")":"(","}":"{","]":"["}
        for c in s:
            if c in closeToOpen:
                if len(stack)!=0 and stack[-1]==closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack)==0
        """stack=[]
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
        return False"""