import sys
input = sys.stdin.readline
from collections import deque

N,M,K = map(int,input().split())
graph = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(K):
    r,c = map(int,input().split())
    graph[r-1][c-1] = 1

visited = [[0 for _ in range(M)] for _ in range(N)]
d = [(0,1),(1,0),(0,-1),(-1,0)]

def bfs(a,b):
    queue = deque()
    queue.append((a,b))
    visited[a][b] = 1
    cnt = 1
    while queue:
        x,y = queue.popleft()
        for dx,dy in d:
            if 0<=x+dx<N and 0<=y+dy<M and not visited[x+dx][y+dy] and graph[x+dx][y+dy] == 1:
                cnt += 1
                queue.append((x+dx,y+dy))
                visited[x+dx][y+dy] = 1
    return cnt

answer = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j] and graph[i][j] == 1:
            answer = max(answer,bfs(i,j))

print(answer)