#그래프 2개 해서 일괄적으로 줄여야할듯
import sys
input = sys.stdin.readline
from collections import deque

def check(x,y):
    queue = deque([(x,y)])
    visited[x][y] = 1
    while queue:
        curr_x, curr_y = queue.popleft()
        for dx,dy in d:
            if 0<=curr_x+dx<N and 0<=curr_y+dy<M and graph[curr_x+dx][curr_y+dy] and not visited[curr_x+dx][curr_y+dy]:
                visited[curr_x+dx][curr_y+dy] = 1
                queue.append((curr_x+dx,curr_y+dy))


N,M = map(int,input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))

d = [(0,1),(1,0),(0,-1),(-1,0)]
answer = 0
while True:
    answer+=1
    melt = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            for x,y in d:
                dx = i+x
                dy = j+y
                if 0<=dx<N and 0<=dy<M and graph[dx][dy] == 0:
                    melt[i][j] -=1

    for i in range(N):
        for j in range(M):
            graph[i][j] += melt[i][j]
            if graph[i][j]<0:
                graph[i][j] = 0

    visited = [[0 for _ in range(M)] for _ in range(N)]
    cnt = 0
    flag = False
    for i in range(N):
        if flag:
            break
        for j in range(M):
            if graph[i][j] and not visited[i][j]:
                if cnt == 1:
                    flag = True
                    break
                else:
                    check(i,j)
                    cnt+=1
    if flag:
        break
    if cnt == 0:
        answer = 0
        break
print(answer)





