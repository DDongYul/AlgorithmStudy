#임의의 값 하나만 탐색해도 됨, 나머지는 어차피 연결되어있음
#wires에서 값 하나 pop하고 탐색하면 BFS 돌리면 될듯
from collections import deque

def BFS(wires):
    graph = [[] for _ in range(len(wires)+2)]
    for a,b in wires:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    queue = deque()
    queue.append(0)
    visited = [0 for _ in range(len(wires)+2)]
    while queue:
        curr = queue.popleft()
        if not visited[curr]:
            for i in graph[curr]:
                queue.append(i)
            visited[curr] = 1
    return abs((len(wires)+2 - sum(visited))-sum(visited))

def solution(n, wires):
    answer = n
    for _ in range(n-1):
        temp = wires.pop(0)
        answer = min(answer,BFS(wires))
        wires.append(temp)
    return answer