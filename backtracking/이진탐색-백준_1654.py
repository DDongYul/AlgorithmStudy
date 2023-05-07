#start는 무조건 되는 경우, end는 무조건 안되는 경우로 범위 잡아서 이진탐색
import sys
input = sys.stdin.readline
k,n = map(int,input().split())
lan = []
for _ in range(k):
    lan.append(int(input()))

start = 1
end = max(lan)
while start<=end:
    cnt = 0
    mid = (start+end)//2
    for i in lan:
        cnt+=int(i/mid)
    if cnt>=n:
        start = mid+1
    else:
        end = mid-1
print(end)