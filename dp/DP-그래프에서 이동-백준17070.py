import sys
input = sys.stdin.readline

rst = 0
def DFS(x,y,flag):      #flag 0:대각선 1:가로 2:세로
    global rst
    if x == N-1 and y == N-1:
        rst+=1
    if y+1<=N-1 and not graph[x][y+1] and flag!=2:      #가로
        DFS(x,y+1,1)
    if x+1<=N-1 and y+1<=N-1 and not graph[x+1][y+1] and not graph[x][y+1] and not graph[x+1][y]:   #대각선
        DFS(x+1,y+1,0)
    if x+1<=N-1 and not graph[x+1][y] and flag != 1:    #세로
        DFS(x+1,y,2)

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))

dp = [[[0 for _ in range(3)] for _ in range(N)]for _ in range(N)] #dp[row][col][상태] #대각0 가로 1 세로 2
dp[0][1][1] = 1
for i in range(2,N):
    if graph[0][i] == 0:
        dp[0][i][1] = dp[0][i-1][1]

for i in range(1,N):
    for j in range(1,N):
        if not graph[i][j] and not graph[i][j-1] and not graph[i-1][j]:
            dp[i][j][0] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]
        if not graph[i][j]:
            dp[i][j][1] = dp[i][j-1][1]+ dp[i][j-1][0]
            dp[i][j][2] = dp[i-1][j][2]+ dp[i-1][j][0]

print(dp[N-1][N-1][0] + dp[N-1][N-1][1] + dp[N-1][N-1][2])

# DFS(0,1,1)
# print(rst)
