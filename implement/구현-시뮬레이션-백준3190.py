import sys
input = sys.stdin.readline

#0:우 1:하 2:좌 3:상
d = [[0,1],[1,0],[0,-1],[-1,0]]
def move(x,y,direction):
    global answer
    dx,dy = d[direction]
    dx = x+dx
    dy = y+dy
    if 0<=dx<N and 0<=dy<N:
        head[0] = dx
        head[1] = dy
        if graph[dx][dy] == 0:
            snake.append([dx,dy])
            graph[dx][dy] = 2
            rx,ry = snake.pop(0)
            graph[rx][ry] = 0
            answer+=1
            return True
        elif graph[dx][dy] == 1:
            snake.append([dx, dy])
            graph[dx][dy] = 2
            answer+=1
            return True
        elif graph[dx][dy] == 2:
            return False
    else:
        return False

N = int(input())
K = int(input())
graph = [[0 for _ in range(N)] for _ in range(N)]
turn = []

for _ in range(K):
    X,Y = map(int,input().split())
    graph[X-1][Y-1] = 1

L = int(input())
for _ in range(L):
    R,C = input().split()
    turn.append([int(R),C])

head = [0,0]
snake = [[0,0]] #자기 자신
graph[0][0] = 2
curr_dir = 0 #0:우 1:하 2:좌 3:상
flag = True
answer = 1
index = 0

while flag:
    if answer-1==turn[index][0]:
        if turn[index][1] == 'D':
            curr_dir+=1
            if curr_dir>3:
                curr_dir = 0
        elif turn[index][1] == 'L':
            curr_dir-=1
            if curr_dir<0:
                curr_dir = 3
        if index<len(turn)-1:
            index+=1
    flag = move(head[0],head[1],curr_dir)

print(answer)
