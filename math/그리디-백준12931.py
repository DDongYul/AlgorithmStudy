#2로 나누어지면 우선 다 나누고 안나누어 떨어지는게 있으면 1 뺌
import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int,input().split()))
cnt = 0
while sum(lst)!=0:
    for i in range(len(lst)):
        if lst[i]%2:
            lst[i]-=1
            cnt+=1
    if sum(lst) == 0:
        break
    for i in range(len(lst)):
        lst[i] = lst[i]//2
    cnt+=1
print(cnt)