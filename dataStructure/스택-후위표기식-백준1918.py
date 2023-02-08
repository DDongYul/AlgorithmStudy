expression = list(input().rstrip())
stack = []
rst = ''
for s in expression:
    if s == '(':
        stack.append(s)
    elif s == '*' or s == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            rst += stack.pop()
        stack.append(s)
    elif s == '+' or s == '-':
        while stack and stack[-1] != '(':
            rst += stack.pop()
        stack.append(s)
    elif s == ')':
        while stack and stack[-1] != '(':
            rst += stack.pop()
        stack.pop()
    else:
        rst+=s
while stack :
    rst+=stack.pop()

print(rst)