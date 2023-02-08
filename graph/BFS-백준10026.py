import sys
from collections import deque

N = int(input())
graph = []
graph2 = [[] for _ in range(N)]
for i in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))       #!색약

for i in range(0,N):
    for j in range(0,N):
        if graph[i][j] == 'G':
            graph2[i].append('R')
        else:
            graph2[i].append(graph[i][j])                   #색약

visited = [[0 for _ in range(N)] for _ in range(N)]         #!색약
visited2 = [[0 for _ in range(N)] for _ in range(N)]        #색약

#일반인 전용
def Search(n):
    queue = deque()
    queue.append(n)
    while queue:
        x,y = queue.popleft()
        color = graph[x][y]
        direction = [[x-1,y],[x+1,y],[x,y-1],[x,y+1]]
        for j in direction:
            x1 = j[0]
            y1 = j[1]
            if 0<= x1<=N-1 and 0<= y1 <=N-1 and not visited[x1][y1] and graph[x1][y1] == color:
                queue.append((x1,y1))
                visited[x1][y1] = 1

#색약 전용
def Search2(n):
    queue = deque()
    queue.append(n)
    while queue:
        x,y = queue.popleft()
        color = graph2[x][y]
        direction = [[x-1,y],[x+1,y],[x,y-1],[x,y+1]]
        for j in direction:
            x1 = j[0]
            y1 = j[1]
            if 0<= x1<=N-1 and 0<= y1 <=N-1 and not visited2[x1][y1] and graph2[x1][y1] == color:
                queue.append((x1,y1))
                visited2[x1][y1] = 1

count = count2 = 0
for i in range(0,N):
    for j in range(0,N):
        if visited[i][j] == 0:
            Search((i,j))
            count+=1

for i in range(0,N):
    for j in range(0,N):
        if visited2[i][j] == 0:
            Search2((i,j))
            count2+=1

print(count,count2)

