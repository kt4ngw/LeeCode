class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        stackPiont = -1
        flag = 0
        for i in s:
            if i == '[' or i == '(' or i == '{':  # 遇到左括号就进栈
                stack.append(i)
                stackPiont += 1
            else:  # 遇到右括号
                if (i == ']' or i == '}' or i == ')') and stackPiont == -1:
                    flag = 1
                    break
                if i == ']' and stack[stackPiont] == '[':
                    stack.pop()
                    stackPiont -= 1
                elif i == ')' and stack[stackPiont] == '(':
                    stack.pop()
                    stackPiont -= 1
                elif i == '}' and stack[stackPiont] == '{':
                    stack.pop()
                    stackPiont -= 1
                else:
                    stack.append(i)
                    stackPiont += 1

        if stackPiont != -1 or flag == 1:
            return False
        else:
            return True
