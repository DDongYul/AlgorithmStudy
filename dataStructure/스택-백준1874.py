#주어진 값 스택에서 뽑으면서 진행 주어진 값 왼쪽스택 결과값 오른쪽 스택
# curr 보다 값이 크면 왼쪽 스택에 그 값까지 push, 그 값 도달하면 pop한번 해서 우스택 넣기 curr은 그 값으로 갱신
# 다음 값이 curr보다 작으면 왼스택 pop 이때 pop한 값이 다음 값과 같아야함 크면 위 과정 반복
import sys
input = sys.stdin.readline
stack1 = []
stack2 = []
answer = []
n = int(input())
cnt = 0
flag = True
for i in range(n):
    curr = int(input())
    if cnt<curr:
        while cnt<curr:
            cnt+=1
            stack1.append(cnt)
            answer.append('+')
        if cnt == curr:
            stack2.append(stack1.pop())
            answer.append('-')
    else:
        num = stack1.pop()
        if curr == num:
            stack2.append(num)
            answer.append('-')
        else:
            flag = False
if flag:
    for i in answer:
        print(i)
else:
    print("NO")


