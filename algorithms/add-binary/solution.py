class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {"}" : "{", ")" : "(", "]" : "["}
        for x in s:
            if x in "[{(" :
                stack.append(x)
            else:
                if len(stack) == 0:
                    return False
                elif stack[-1] == matching[x] :
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False
        
        