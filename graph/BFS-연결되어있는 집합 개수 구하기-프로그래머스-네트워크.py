# 연결 되어있는 집합의 개수
# BFS 돌리고 visited 0인 요소들 BFS 돌리고 돌린 횟수 return
from collections import deque

def BFS(start, edges, visited):
    queue = deque()
    queue.append(start)
    while queue:
        curr = queue.popleft()
        if not visited[curr]:
            visited[curr] = 1
            for i in range(len(edges[curr])):
                if edges[curr][i] == 1 and not visited[i]:
                    queue.append(i)
    return visited

def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]
    while not all(visited):
        for i in range(n):
            if visited[i] == 0:
                visited = BFS(i, computers, visited)
                answer += 1
                break
    return answer