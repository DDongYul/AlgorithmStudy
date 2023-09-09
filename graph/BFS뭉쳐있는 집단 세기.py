import sys
input = sys.stdin.readline
from collections import deque

def bfs(i,j):
    global cnt
    cnt+=1
    temp = 1
    queue = deque()
    queue.append((i,j))
    d = [(0,1),(0,-1),(1,0),(-1,0)]
    while queue:
        x,y = queue.popleft()
        for dx,dy in d:
            if 0<=x+dx<n and 0<=y+dy<n and not visited[x+dx][y+dy] and graph[x+dx][y+dy] =='1':
                queue.append((x+dx,y+dy))
                visited[x+dx][y+dy] = 1
                temp+=1
    return temp

ans = []
graph = []
n = int(input())
for _ in range(n):
    graph.append(input().rstrip())

cnt = 0
visited = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == '1':
            visited[i][j] = 1
            ans.append(bfs(i,j))

ans.sort()
print(cnt)
for i in ans:
    print(i)


