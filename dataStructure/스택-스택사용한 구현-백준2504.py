S = input()
li = []
level_li = [0]*20
level = 0

flag = True
for i in S:
    if i == '(' or i == '[':
        li.append(i)
    elif i == ')':
        if len(li) == 0:
            flag = False
            break
        elif li.pop() == '[':
            flag=False
            break
    elif i == ']':
        if len(li) == 0:
            flag = False
            break
        if li.pop() == '(':
            flag=False
            break
if flag:
    for i in S:
        if i == '(' or i == '[':
            li.append(i)
            level+=1
        elif i == ')' or i == ']':
            if li.pop() == '(':
                temp = 2
            else:
                temp = 3
            if level_li[level+1]==0:
                level_li[level] += temp        #괄호가 바로 닫히는 경우
                level -=1
            else:
                level_li[level] += temp*level_li[level+1]
                level_li[level+1] = 0
                level -=1
                                        #괄호안에 괄호가 있는 경우
    print(level_li[1])
else:
    print(0)