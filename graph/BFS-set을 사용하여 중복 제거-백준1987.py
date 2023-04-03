import sys
input = sys.stdin.readline
from collections import deque

answer = 0
d = [(0,1),(1,0),(0,-1),(-1,0)]
n,m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(input()))
queue = set([(0,0,graph[0][0])])

while queue:
    x,y,visited = queue.pop()
    answer=max(answer,len(visited))
    for dx, dy in d:
        nx = x+dx
        ny = y+dy
        if (0<=nx<n) and (0<=ny<m) and graph[nx][ny] not in visited:
            queue.add((nx,ny,visited + graph[nx][ny]))

print(answer)
