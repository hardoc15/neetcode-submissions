class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i == "+":
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif i == "-":
                right = stack.pop()
                left = stack.pop()
                stack.append(int(left)-int(right))
            elif i == "*":
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif i == "/":
                right = stack.pop()
                left = stack.pop()
                stack.append(int(left)/int(right))
            else:
                stack.append(int(i))
        return int(stack[0])
                
        