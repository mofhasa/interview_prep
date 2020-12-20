class HRMedium_set1:
    #LC valid parentheses
    def p1(self, s):
        stack = []
        for x in s:
            if x == '{' or x == '[' or x == '(':
                stack.append(x)
            elif x == '}' or x == ']' or x == ')':
                try:
                    if x == '}' and stack[-1] == "{":
                        stack.pop()
                    elif x == ']' and stack[-1] == "[":
                        stack.pop()
                    elif x == ')' and stack[-1] == "(":
                        stack.pop()
                    else:
                        return False
                except IndexError:
                    return False
        return len(stack) == 0



