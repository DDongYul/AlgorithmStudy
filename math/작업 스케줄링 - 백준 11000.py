import sys

input = sys.stdin.readline
from heapq import heappush, heappop

N = int(input())
works = []
for _ in range(N):
    a, b = map(int, input().split())
    works.append((a, b))

works.sort()

# 각 강의실은 끝나는 시간만 기억해두면 됨
room = [0]
for s, e in works:
    curr = heappop(room)
    if curr > s:
        heappush(room, curr)
        heappush(room, e)
    else:
        heappush(room, e)
print(len(room))