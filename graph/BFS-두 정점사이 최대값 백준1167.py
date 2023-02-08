#트리의 지름: 임의의 한 점에서 가장 먼 점 -> 거기서 가장 먼 점 (DFS 사용)
import sys
from collections import deque

def BFS(start):
    visited = [0 for _ in range(n+1)]
    depth = [0 for _ in range(n+1)]
    visited[start] = 1
    queue = deque()
    queue.append((start,0))
    while queue:
        curr,w = queue.popleft()
        for d,ww in edge[curr]:
            if not visited[d]:
                queue.append((d,w+ww))
                visited[d] = 1
                depth[d] = w+ww

    return depth

input = sys.stdin.readline
n = int(input())
edge = [[]for _ in range(n+1)]
for i in range(n):
    temp = list(map(int,input().split()))
    v = temp[0]
    j=1
    for _ in range(int((len(temp)-2)/2)):
        edge[v].append((temp[j],temp[j+1]))
        j+=2

v1 = BFS(1)
s = v1.index(max(v1))
v2 = BFS(s)
print(max(v2))





