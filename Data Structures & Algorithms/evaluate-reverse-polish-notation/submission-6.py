class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == '-' or i == '+' or i =='/' or i=='*':
                b = stack.pop()
                a = stack.pop()
                if i =="+":
                    c = a + b
                elif i=='-':
                    c = a - b
                elif i=='*':
                    c = a*b
                else:
                    c = a/b
                stack.append(int(c))
                print(c)
            else:
                stack.append(int(i))
        return stack[-1]