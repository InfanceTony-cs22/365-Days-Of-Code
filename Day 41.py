class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        stack = []
        operators = {'+', '-', '*', '/'}

        for token in A:
            if token in operators:
                operand2 = stack.pop()
                operand1 = stack.pop()
                if token == '+':
                    result = operand1 + operand2
                elif token == '-':
                    result = operand1 - operand2
                elif token == '*':
                    result = operand1 * operand2
                else:
                    result = int(operand1 / operand2)
                stack.append(result)
            else:
                stack.append(int(token))

        return stack.pop()
