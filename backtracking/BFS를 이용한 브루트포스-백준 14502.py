# 값이 0인 것 중 3개 뽑기 그래프에 반영 후 BFS
import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque

d = [(0,-1),(-1,0),(0,1),(1,0)]
def BFS(s,e,grp):
    queue = deque()
    queue.append((s,e))
    visited[s][e] = 1
    while queue:
        curr = queue.popleft()
        for dx,dy in d:
            dx = curr[0] + dx
            dy = curr[1] + dy
            if 0<=dx<N and 0<=dy<M and grp[dx][dy] == 0 and not visited[dx][dy]:
                queue.append((dx,dy))
                visited[dx][dy] = 1
                grp[dx][dy] = 2

def count(grp):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if grp[i][j] == 0:
                cnt+=1
    return cnt

N,M = map(int,input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))

empty = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            empty.append((i,j))

answer = 0
grp = [[0 for _ in range(M)] for _ in range(N)]
wall = list(combinations(empty,3))
for a,b,c in wall:
    visited = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            grp[i][j] = graph[i][j]
    grp[a[0]][a[1]] = 1
    grp[b[0]][b[1]] = 1
    grp[c[0]][c[1]] = 1
    for i in range(N):
        for j in range(M):
            if grp[i][j] == 2 and not visited[i][j]:
                BFS(i,j,grp)
    answer = max(answer,count(grp))

print(answer)

