# 문제는 S->L->E순서지만 레버에서 BFS 한번만 돌리면 해결 가능
#visited 선언할때 안쪽이 n 바깥쪽이 m인데 바꿔서 했다가 틀렸었음
from collections import deque

def solution(maps):
    m = len(maps)
    n = len(maps[0])
    for i in range(m):
        for j in range(n):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'E':
                end = (i, j)
            elif maps[i][j] == 'L':
                lever = (i, j)
    # BFS
    queue = deque()
    visited = [[0 for _ in range(n)] for _ in range(m)] #안쪽이 n 바깥쪽이 m!!!!!
    visited[lever[0]][lever[1]] = 1
    queue.append(lever)

    d = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    while queue:
        x, y = queue.popleft()
        curr = visited[x][y]
        for mx, my in d:
            dx = x + mx
            dy = y + my
            if 0 <= dx < m and 0 <= dy < n and maps[dx][dy] != 'X' and not visited[dx][dy]:
                visited[dx][dy] = curr + 1
                queue.append((dx, dy))

    if visited[start[0]][start[1]] == 0 or visited[end[0]][end[1]] == 0:
        return -1
    else:
        return visited[start[0]][start[1]] + visited[end[0]][end[1]] - 2