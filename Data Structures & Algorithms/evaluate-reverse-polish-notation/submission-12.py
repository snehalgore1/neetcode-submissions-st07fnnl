class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for t in tokens:
            if t not in '+-*/':
                s.append(int(t))
            else:
                num2 = s.pop()
                num1 = s.pop()
                if t =='+':
                    s.append(num1+num2)
                elif t =='-':
                    s.append(num1-num2)
                elif t =='*':
                    s.append(num1*num2)
                else:
                    s.append(int(num1/num2))
        return s[-1]