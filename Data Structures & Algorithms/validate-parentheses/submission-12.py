class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        p = {"}":"{", ")":"(","]":"["}

        for i in s:
            if not stack and i not in p:
                stack.append(i)
                continue
            
            if i in p and stack:
                if stack[-1] == p[i]:
                    stack.pop()
                    continue
                else:
                    return False
            stack.append(i)
                
        
        return not stack
            

        
    


        
        
        



        
        

                