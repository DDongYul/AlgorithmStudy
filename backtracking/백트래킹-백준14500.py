#네가지 방향 백트래킹
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
graph = []
visited = [[0 for _ in range(M)]for _ in range(N)]

for _ in range(N):
    graph.append(list(map(int,input().split())))

def search(x,y,depth,val):
    global rst
    if depth==4:
        rst = max(rst,val)
        return
    for d in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
        dx = d[0]
        dy = d[1]
        if 0 <= dx < N and 0 <= dy < M and not visited[dx][dy]:
            val2 = val + graph[dx][dy]
            visited[dx][dy] = 1
            search(dx,dy,depth+1,val2)
            visited[dx][dy]=0

def search2(x,y,val):
    global rst
    temp = []
    for d in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
        dx = d[0]
        dy = d[1]
        if 0 <= dx < N and 0 <= dy < M and not visited[dx][dy]:
            temp.append(graph[dx][dy])
    if len(temp)==4:
        rst = max(rst,(val+sum(temp)-min(temp)))
    elif len(temp) == 3:
        rst = max(rst,val+sum(temp))
    else:
        return

rst = 0
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        search(i,j,1,graph[i][j])
        visited[i][j] = 0
        search2(i,j,graph[i][j])

print(rst)