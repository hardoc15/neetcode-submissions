class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        dict1 = {"}":"{",")":"(","]":"["}

        for i in s:
            if not stack:
                stack.append(i)
                continue
            if i in dict1:
                j = stack.pop()
                if dict1[i] != j:
                    return False
            else:
                stack.append(i)
        return len(stack) == 0