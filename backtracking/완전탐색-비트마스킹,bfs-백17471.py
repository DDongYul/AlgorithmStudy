#비트마스킹 이용해서 두개로 나누고 두개가 모두 연결돼있으면 통과
#구역의 인구 차이 두번재 줄
import sys
from collections import deque
input = sys.stdin.readline

def bfs(lst):
    if len(lst) == 1:
        return True
    start = lst[0]
    visited = [0 for _ in range(len(graph))]
    queue = deque()
    queue.append(start)
    while queue:
        curr = queue.popleft()
        for i in graph[curr]:
            if not visited[i-1]:
                queue.append(i-1)
                visited[i-1] = 1
    for i in lst:
        if visited[i] == 0:
            return False
    return True


n = int(input())
p = list(map(int,input().split()))
graph = [[] for _ in range(n)]
answer = sys.maxsize
for i in range(n):
    graph[i] = list(map(int,input().split()))[1:]

for i in range(1,pow(2,n)-1):
    bit = bin(i)[2:]
    while len(bit)<n:
        bit = '0' + bit
    left = []
    right = []
    for j in range(len(bit)):
        if bit[j] == '0':
            left.append(j)
        else:
            right.append(j)
    if bfs(left) and bfs(right):
        cl = 0
        cr = 0
        for i in left:
            cl+=p[i]
        for i in right:
            cr+=p[i]
        answer = min(answer,abs(cl-cr))
        # print(left,right)

if answer == sys.maxsize:
    print(-1)
else:
    print(answer)
