# 가장 큰 수 찾아서 얘 기준으로 정렬 두번
# 1 2 3 / 4  4 / 3 1
import sys
input = sys.stdin.readline
N = int(input())
S = list(map(int,input().split()))
mx = max(S)
lst = [0 for _ in range(mx+1)]
for i in S:
    lst[i]+=1
answer = 0
for i in range(mx+1):
    if lst[i]>1:
        answer+=2
    elif lst[i] == 1:
        answer+=1

print(answer)