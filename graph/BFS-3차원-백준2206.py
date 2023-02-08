import sys
input = sys.stdin.readline
from collections import deque
d = [(-1,0),(1,0),(0,-1),(0,1)]

def DFS():
    visited = [[[0 for _ in range(2)] for _ in range(M)] for _ in range(N)] #위치[0] -> 벽을 한번도 안부숨 위치[1]-> 벽을 한번 부숨
    visited[0][0][0] = 1
    visited[0][0][1] = 1
    queue = deque()
    queue.append((0,0,0,1))
    while queue:
        x,y,flag,w = queue.popleft()    #flag = 0: 벽을 한번도 안뷰 1: 이전에 부숨
        if x == N-1 and y==M-1:
            return visited[x][y][flag]
        for dx,dy in d:
            if 0<=x+dx<=N-1 and 0<=y+dy<=M-1 and not visited[x+dx][y+dy][flag]:
                if graph[x + dx][y + dy] == 0:  #지나려는 점이 0이면 그냥 지나도 됨
                    queue.append((x+dx,y+dy,flag,w+1))
                    visited[x+dx][y+dy][flag] = w+1
                else:                   #지나려는 점이 1, 이미 부순상태면 못지나감, 안부순 상태면 부수고감
                    if flag:
                        continue
                    else:
                        queue.append((x+dx, y+dy, 1, w+1))    #벽을 부수고 지나감
                        visited[x + dx][y + dy][1] = w + 1

    return -1


N,M = map(int,input().split())
graph = []
for _ in range(N):
    temp = input().rstrip()
    temp_list=[]
    for i in temp:
        temp_list.append(int(i))
    graph.append(temp_list)

print(DFS())
