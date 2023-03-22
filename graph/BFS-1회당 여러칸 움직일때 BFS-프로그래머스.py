from collections import deque

INF = 1000000000
def solution(board):
    mx = len(board)
    my = len(board[0])
    # BFS를 하는데 한번의 이동이 끝까지 가야한다 visit은 멈춘 구간
    visited = [[INF for _ in range(my)] for _ in range(mx)]

    for i in range(mx):
        for j in range(my):
            if board[i][j] == 'R':
                visited[i][j] = 0
                start = (i, j)
            if board[i][j] == 'G':
                gx=i
                gy=j

    queue = deque()
    queue.append(start)

    while queue:
        x, y = queue.popleft()
        d = visited[x][y]

        dx = x
        #위로 진행 다음 좌표 값이 0보다 작거나, D면 진행하지 못함
        while dx>=0:
            if dx==0 or board[dx-1][y] == 'D':
                if board[dx][y] == 'G':
                    visited[dx][y] = min(visited[dx][y],d+1)
                    break
                else:
                    if visited[dx][y] == INF:
                        visited[dx][y] = d + 1
                        queue.append((dx,y))
                    break
            dx-=1

        #좌
        dy = y
        while dy>=0:
            if dy==0 or board[x][dy-1] == 'D':
                if board[x][dy] == 'G':
                    visited[x][dy] = min(visited[x][dy],d+1)
                    break
                else:
                    if visited[x][dy] == INF:
                        visited[x][dy] = d + 1
                        queue.append((x,dy))
                    break
            dy-=1

        #하
        dx = x
        while dx <= mx-1:
            if dx == mx-1 or board[dx + 1][y] == 'D':
                if board[dx][y] == 'G':
                    visited[dx][y] = min(visited[dx][y], d + 1)
                    break
                else:
                    if visited[dx][y] == INF:
                        visited[dx][y] = d + 1
                        queue.append((dx, y))
                    break
            dx += 1

        # 우
        dy = y
        while dy <= my-1:
            if dy == my-1 or board[x][dy + 1] == 'D':
                if board[x][dy] == 'G':
                    visited[x][dy] = min(visited[x][dy], d + 1)
                    break
                else:
                    if visited[x][dy] == INF:
                        visited[x][dy] = d + 1
                        queue.append((x, dy))
                    break
            dy += 1

    answer = visited[gx][gy]
    if answer == INF:
        return -1
    return answer

print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))
print(solution([".D.R", "....", ".G..", "...D"]))

