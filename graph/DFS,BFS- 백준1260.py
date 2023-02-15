from collections import deque
import sys

N,M,V = map(int,input().split())
data = [[]for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,sys.stdin.readline().split())
    data[a].append(b)
    data[b].append(a)

for j in range(N+1):
    data[j].sort()

def DFS(graph,n,start):
    visited = [0 for _ in range(n+1)]
    result = []
    queue = deque()
    queue.append(start)
    while queue:
        curr = queue.pop()
        if not visited[curr]:
            visited[curr] = 1
            result.append(curr)
            for node in graph[curr][::-1]:
                if not visited[node]:
                    queue.append(node)
    return result

def BFS(graph,n,start):
    visited = [0 for _ in range(n+1)]
    visited[start] = 1
    result = []
    queue = deque()
    queue.append(start)
    while queue:
        curr = queue.popleft()
        result.append(curr)
        for node in graph[curr]:
            if not visited[node]:
                queue.append(node)
                visited[node] = 1
    return result

print(" ".join(map(str,DFS(data,N,V))))
print(" ".join(map(str,BFS(data,N,V))))