import sys
from collections import deque

N,K = map(int,sys.stdin.readline().split())

queue = deque()
visited = [False]*100001
depth = [0]*100001
queue.append(N)
visited[N] = True

while queue:
    curr = queue.popleft()
    if curr == K:
        print(depth[curr])
        break
    if curr+1 <=100000 and not visited[curr+1]:
        queue.append(curr+1)
        depth[curr+1] = depth[curr]+1
        visited[curr+1] = True
    if curr*2 <=100000 and not visited[curr*2]:
        queue.append(curr*2)
        depth[curr*2] = depth[curr]+1
        visited[curr*2] = True
    if curr-1 >= 0 and not visited[curr-1]:
        queue.append(curr-1)
        depth[curr-1] = depth[curr]+1
        visited[curr-1] = True
