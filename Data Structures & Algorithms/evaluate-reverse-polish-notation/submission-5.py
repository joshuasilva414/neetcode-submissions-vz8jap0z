class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ['+','-','*','/']
        stack = []
        for t in tokens:
            if t not in ops:
                stack.append(int(t))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                match t:
                    case '+':
                        stack.append(op1 + op2)
                    case '-':
                        stack.append(op1 - op2)
                    case '*':
                        stack.append(op1 * op2)
                    case '/':
                        stack.append(int(op1 / op2))
        return stack[-1]