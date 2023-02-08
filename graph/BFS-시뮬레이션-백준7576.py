import sys
from collections import deque
input = sys.stdin.readline
M,N = map(int,sys.stdin.readline().split())
graph = []
for i in range(N):
    graph.append(list(map(int,input().split())))

queue = deque()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i,j,1))

visited = [[0]*M for _ in range(N)]

for i in queue:
    visited[i[0]][i[1]] = 1
while queue:
    x,y,depth = queue.popleft()
    for d in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
        dx =d[0]
        dy = d[1]
        if 0<=dx<N and 0<=dy<M:
            if not visited[dx][dy] and graph[dx][dy] != -1:
                queue.append((dx,dy,depth+1))
                graph[dx][dy]=depth+1
                visited[dx][dy] = 1

flag = False
rst = 0
for i in graph:
    for j in i:
        if j==0:
            flag = True
        if rst<j:
            rst = j
if flag:
    print(-1)
else:
    print(rst-1)





