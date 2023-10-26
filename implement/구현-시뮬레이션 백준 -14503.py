import sys
input = sys.stdin.readline

d = [[-1,0],[0,1],[1,0],[0,-1]] #북동남서
cnt = 2
def move(x,y,direction):
    global cnt
    if graph[x][y] == 0:
        graph[x][y] = cnt
        cnt+=1
        return x, y, direction
    flag = False
    for dx,dy in d:
        dx+=x
        dy+=y
        if 0<=dx<N and 0<=dy<M and not graph[dx][dy]: #case 3
            flag = True
            break
    if flag:
        for _ in range(4):
            direction-=1
            if direction<0:
                direction = 3
            if graph[x+d[direction][0]][y+d[direction][1]] == 0:
                return x+d[direction][0], y+d[direction][1], direction
    else:
        if direction==2:
            bacDir = 0
        elif direction == 3:
            bacDir = 1
        else:
            bacDir = direction+2
        dx,dy = d[bacDir]
        dx += x
        dy += y
        if 0 <= dx < N and 0 <= dy < M and graph[dx][dy]!= 1:
            return dx,dy,direction
        return -1,-1,-1
    return -1,-1,-1

N,M = map(int, input().split()) # N이 세로 M이 가로
r,c,dr = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))

while True:
    r,c,dr = move(r,c,dr) #r 세로, c 가로
    if r==-1:
        break
print(cnt-2)






