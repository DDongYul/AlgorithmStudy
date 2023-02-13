from collections import deque


def solution(maps):
    answer = []
    queue = deque()
    m = len(maps)
    n = len(maps[0])
    visited = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if not visited[i][j] and maps[i][j] != 'X':
                queue.append((i, j))
                food = 0
                while queue:
                    x, y = queue.popleft()
                    if not visited[x][y]:
                        food += int(maps[x][y])
                        visited[x][y] = 1
                        for dx, dy in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                            if 0 <= dx < m and 0 <= dy < n and not visited[dx][dy] and maps[dx][dy] != 'X':
                                queue.append((dx, dy))
                answer.append(food)
    if answer:
        return sorted(answer)
    else:
        return [-1]

# mapp = ["X591X","X1X5X","X231X", "1XXX1"]
# print(solution(mapp))



