import sys
input = sys.stdin.readline
from collections import deque


def BFS(start, end):
    d = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
    queue = deque()
    queue.append((start,end))
    visited[start][end] = 1
    while queue:
        x,y = queue.popleft()
        for dx,dy in d:
            dx = x+dx
            dy = y+dy
            if 0<=dx<h and 0<=dy<w and not visited[dx][dy] and graph[dx][dy]:
                visited[dx][dy] = 1
                queue.append((dx,dy))


while True:
    w,h = map(int,input().split())
    if w==0 and h ==0:
        break
    graph = []
    for _ in range(h):
        graph.append(list(map(int,input().split())))
    visited = [[0 for _ in range(w)] for _ in range(h)]
    answer = 0
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and graph[i][j] == 1:
                BFS(i,j)
                answer+=1
    print(answer)




