import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            start = (i,j)

dist = [[-1 for _ in range(m)] for _ in range(n)]
dist[start[0]][start[1]] = 0
queue = deque()
queue.append(start)
d = [(0,1),(1,0),(0,-1),(-1,0)]
while queue:
    x,y = queue.popleft()
    for mx,my in d:
        dx = x+mx
        dy = y+my
        if 0<=dx<n and 0<=dy<m and dist[dx][dy] == -1:
            if graph[dx][dy] == 1:
                dist[dx][dy] = dist[x][y] + 1
                queue.append((dx,dy))
            elif graph[dx][dy] == 0:
                dist[dx][dy] = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and dist[i][j] == -1:
            dist[i][j] = 0



for i in dist:
    for j in i:
        print(j,end = ' ')
    print()
