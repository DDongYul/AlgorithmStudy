import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n)]
for i in range(n):
    temp = list(input().rstrip())
    for j in temp:
        graph[i].append(int(j))

visited = [[0 for _ in range(m)] for _ in range(n)]
visited[0][0] = 1
queue = deque()
queue.append([0,0])
d = [(0,1),(0,-1),(1,0),(-1,0)]
while queue:
    x,y = queue.popleft()
    for dx,dy in d:
        nx = x+dx
        ny = y+dy
        if 0<=nx<=n-1 and 0<=ny<=m-1 and graph[nx][ny] == 1 and not visited[nx][ny]:
            queue.append([nx,ny])
            visited[nx][ny] = visited[x][y] + 1

print(visited[n-1][m-1])

