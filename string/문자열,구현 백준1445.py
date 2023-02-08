import sys
from heapq import heappush,heappop
input = sys.stdin.readline
N,M = map(int,input().split())
graph = []
for _ in range(N):
    graph.append(list(input().strip()))

d = [(0,-1),(0,1),(-1,0),(1,0)]
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'S':
            start = (0,0,i,j)
        elif graph[i][j] == 'F':
            finish = (i,j)
        elif graph[i][j] == '.':
            graph[i][j] = 1
        elif graph[i][j] == 'g':
            graph[i][j] = 3
            for k in d:
                dx = k[0]
                dy = k[1]
                if 0<=i+dx<N and 0<=j+dy<M:
                    dx+=i
                    dy+=j
                    if graph[dx][dy] != 'g' and graph[dx][dy] != 'F' and graph[dx][dy] != 3 and graph[dx][dy] != 'S':
                        graph[dx][dy] = 2

# for i in graph:
#     print(i)

queue = [start]
flag = True
cost = [[(10000,10000) for _ in range(M)] for _ in range(N)]
cost[start[2]][start[3]] = (0,0)
while queue:
    c1,c2,x,y = heappop(queue)
    if graph[x][y] == 'F':
        break
    for k in d:
        dx = k[0]
        dy = k[1]
        if 0 <= x + dx < N and 0 <= y + dy < M:
            dx += x
            dy += y
            cc1 = c1
            cc2 = c2
            if graph[dx][dy] == 3:
                cc1 +=1
            elif graph[dx][dy] == 2:
                cc2 +=1
            if cc1<cost[dx][dy][0] or (cc1 == cost[dx][dy][0] and cc2<cost[dx][dy][1]):
                cost[dx][dy] = (cc1,cc2)
                heappush(queue, (cc1, cc2, dx, dy))
#
# for i in cost:
#     print(i)
print(cost[finish[0]][finish[1]][0] , cost[finish[0]][finish[1]][1])

# 6 6
# ......
# g..F..
# ......
# gggggg
# ......
# ...S.g