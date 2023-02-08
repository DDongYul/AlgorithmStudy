import sys
input = sys.stdin.readline
from collections import deque

d = [(0,1),(1,0),(0,-1),(-1,0)]
def search():
    inOut = [[0 for _ in range(m)] for _ in range(n)]
    inOut[0][0] = 1
    queue = deque()
    queue.append((0,0))
    while queue:
        x,y = queue.popleft()
        for dx,dy in d:
            if 0<=x+dx<n and 0<=y+dy<m:
                if inOut[x+dx][y+dy] == 0 and graph[x+dx][y+dy] != 1:
                    inOut[x+dx][y+dy] = 1
                    queue.append((x+dx,y+dy))
                elif graph[x+dx][y+dy] == 1:    #외부랑 닿으면 닿은 개수 1 추가
                    inOut[x+dx][y+dy] +=1

    for i in range(n):
        for j in range(m):
            if inOut[i][j]>=2:
                graph[i][j] = 0


n,m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

rst = 0
flag = True
while flag:
    flag = False
    rst+=1
    search()
    for i in range(n):
        for j in range(m):
            if graph[i][j]!=0:
                flag = True
                break

print(rst)

