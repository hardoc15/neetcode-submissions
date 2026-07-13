class Solution:
    def isValid(self, s: str) -> bool:
        groupings = {")" : "(", "]" : "[", "}": "{"}
        stack = []
        i = 0
        for i in s:
            if i in groupings:
                if stack and stack[-1] == groupings[i]:
                    stack.pop(-1)
                else:
                    return False
            else:
                stack.append(i)
        if len(stack) == 0:
            return True
        else:
            return False
        

                