import sys
from collections import deque

def BFS(start,size):
    queue = deque()
    queue.append((start,0))
    visited = [[0 for _ in range(n)] for _ in range(n)]
    depth = [[100000 for _ in range(n)] for _ in range(n)]
    dx = [-1,0,0,1]
    dy = [0,-1,1,0]
    temp = []
    lim_depth = 100000

    while queue:
        curr = queue.popleft()
        x,y = curr[0]
        d = curr[1]
        visited[x][y]=1
        depth[x][y]=d
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and d+1<=lim_depth:
                if graph[nx][ny]==0 or size == graph[nx][ny]:
                    queue.append(((nx,ny),d+1))
                    visited[nx][ny] = 1
                    depth[nx][ny] = d + 1
                elif size>graph[nx][ny]:
                    temp.append((nx, ny, d + 1))
                    lim_depth = d+1
                elif size<graph[nx][ny]:
                    continue
    if temp:
        temp = sorted(temp,key=lambda x: (x[2],x[0],x[1]))
        graph[temp[0][0]][temp[0][1]] = 0
        return temp[0][0],temp[0][1],temp[0][2],1
    else:
        return start[0], start[1], 0, 0

n = int(input())
graph= []
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

cnt = 0
size_cnt = 0
size = 2
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            sx = i
            sy = j
rst = (sx,sy,0,0)
graph[sx][sy]=0
while 1:
    x,y,d,s=rst
    cnt+=d
    size_cnt+=s
    if size_cnt>=size:
        size+=1
        size_cnt=0
    rst = BFS((x,y),size)
    if rst[2]==0:
        break

print(cnt)
