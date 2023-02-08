import sys
from heapq import heappush,heappop
input = sys.stdin.readline
num = 1000000007
T = int(input())
for i in range(T):
    cnt = 1
    n = int(input())
    lst = list(map(int,input().split()))
    lst.sort()
    if n == 1:
        print(1)
        continue
    while n>1:
        a = heappop(lst)
        b = heappop(lst)
        cnt*=(a*b)
        cnt%=num
        heappush(lst,a*b)
        n-=1
    print(cnt)