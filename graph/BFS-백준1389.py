import sys
from collections import deque

def BFS(start):
    visited = [0] * (N + 1)
    queue.append(start)
    while queue:
        curr = queue.popleft()
        for i in edge[curr]:
            if not visited[i]:
                visited[i] = visited[curr]+1
                queue.append(i)
    visited[start] = 0
    return sum(visited)

N,M = map(int,sys.stdin.readline().split())
queue = deque()
edge = [[] for _ in range(N+1)]
result = []

for _ in range(M):
    A,B = map(int,sys.stdin.readline().split())
    edge[A].append(B)
    edge[B].append(A)

for j in range(1,N+1):
    result.append(BFS(j))

print(result.index(min(result))+1)