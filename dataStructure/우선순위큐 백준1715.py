import sys
from heapq import heappush,heappop
input = sys.stdin.readline

N = int(input())
lst = []
rst = 0
for _ in range(N):
    heappush(lst,int(input()))

if N == 1:
    print(0)
    sys.exit()

while len(lst)>1:
    a = heappop(lst)
    b = heappop(lst)
    rst+=(a+b)
    heappush(lst,(a+b))

print(rst)