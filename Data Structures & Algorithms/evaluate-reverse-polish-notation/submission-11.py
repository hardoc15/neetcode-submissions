class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i == "+":
                stack.append(int(stack.pop())+int(stack.pop()))
            elif i == "-":
                r = stack.pop()
                l = stack.pop()
                stack.append(int(l)-int(r))
            elif i == "*":
                stack.append(int(stack.pop())*int(stack.pop()))
            elif i == "/":
                r = stack.pop()
                l = stack.pop()
                stack.append(int(l) / int(r))
            else:
                stack.append(i)
        return int(stack[0])
