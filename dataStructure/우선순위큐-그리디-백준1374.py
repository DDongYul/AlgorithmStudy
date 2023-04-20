import sys
from heapq import heappush,heappop
input = sys.stdin.readline


n = int(input())
study = []
for _ in range(n):
    id,s,e = map(int,input().split())
    study.append((s,e))

study.sort()

room = []
heappush(room, study[0][1])

for i in range(1, n):
    if study[i][0] < room[0]: # 현재 회의실 끝나는 시간보다 다음 회의 시작시간이 빠르면
        heappush(room, study[i][1]) # 새로운 회의실 개설
    else: # 현재 회의실에 이어서 회의 개최 가능
        heappop(room) # 새로운 회의로 시간 변경을 위해 pop후 새 시간 push
        heappush(room, study[i][1])

print(len(room))

