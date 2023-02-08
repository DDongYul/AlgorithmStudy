import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(0,T):
    p = sys.stdin.readline()            #함수
    n = int(sys.stdin.readline())       #리스트 원소 개수
    temp_li = sys.stdin.readline().rstrip()[1:-1].split(",")
    li = deque(temp_li)
    flag = 0 #뒤집힌 상태면 1
    error = 0
    for i in p:
        if flag == 0:
            if i == 'D' and n == 0:
                error = 1
                break
            elif i =='D' and n!=0:
                li.popleft()
                n-=1
            if i =='R':
                flag = 1
        elif flag == 1:
            if i == 'D' and n == 0:
                error=1
                break
            elif i =='D' and n!=0:
                li.pop()
                n-=1
            if i =='R':
                flag = 0
    if error ==1:
        print("error")
    elif error == 0 and flag == 0:
        print("[" + ",".join(li) + "]")
    elif error == 0 and flag == 1:
        li.reverse()
        print("[" + ",".join(li) + "]")