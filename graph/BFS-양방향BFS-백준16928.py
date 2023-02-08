import sys
from collections import deque
N,M = map(int,input().split())
ladder = []
snake = []
for _ in range(N):
    ladder.append(list(map(int,sys.stdin.readline().split())))

for _ in range(M):
    snake.append(list(map(int,sys.stdin.readline().split())))

data = [-1 for _ in range(101)]
for x,y in ladder:
    data[x] = y
for x,y in snake:
    data[x] = y

visited = [0 for _ in range(101)]

queue = deque()
queue.append(1)

flag = True
while queue and flag:
    curr = queue.popleft()
    for i in range(curr+1,curr+7):
        if visited[i] == 0:
            visited[i] = visited[curr] + 1
            if data[i] != -1 and visited[data[i]] == 0:
                visited[data[i]] = visited[i]
                queue.append(data[i])
            elif data[i] != -1 and visited[data[i]] !=0:
                visited[data[i]] = min(visited[i], visited[data[i]])
                queue.append(data[i])
            else:
                queue.append(i)


        if i == 100:
            print(visited[100])
            flag = False
            break