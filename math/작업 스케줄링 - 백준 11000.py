import sys
input = sys.stdin.readline
from heapq import heappush, heappop

N = int(input())
work = []
for _ in range(N):
    a,b = map(int,input().split())
    heappush(work, (a,b))

# 각 강의실은 끝나는 시간만 기억해두면 됨
room = [0]
while work:
    s,e = heappop(work) # 작업 스케쥴링: 빠른 시작시간 작업을 우선(Earliest start time first) 배정
    curr = heappop(room)
    if curr>s:
        heappush(room,curr)
        heappush(room,e)
    else:
        heappush(room,e)
print(len(room))