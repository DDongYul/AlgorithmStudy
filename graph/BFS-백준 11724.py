import sys
from collections import deque

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0 for _ in range(N+1)]
visited[0] = 1

def BFS(start):
    queue = deque()
    queue.append(start)
    visited[start] = 1
    while queue:
        curr = queue.popleft()
        for i in graph[curr]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1

cnt = 0
for i in range(1,N+1):
    if not visited[i]:
        BFS(i)
        cnt+=1

print(cnt)