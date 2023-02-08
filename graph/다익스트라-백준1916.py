#백준 1916번 최소비용 구하기
#https://www.acmicpc.net/problem/1916
#우선순위 큐 , 다익스트라
import sys
from heapq import heappush,heappop

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
edge = [[]for _ in range(N+1)]
for _ in range(0,M):
    a,b,c = map(int,sys.stdin.readline().split())
    edge[a].append((b,c))

s,e = map(int,sys.stdin.readline().split())

cost = [100000001]*(N+1)        #최대값 설정
cost[s] = 0                     #시작정점의 비용은 0
heap = []                       #heqpq를 사용하기 위한 리스트 선언
heappush(heap,[0,s])            #우선순위큐의 우선순위를 거리로 맞추기 위해 [정점,비용]이 아닌 [비용,정점] 순으로 넣어줌
                                #deque대신 heapq를 사용하여 1 2 10 / 1 2 5 와같은 상황에서 10이먼저 실행되어 의미없는 연산이 진행되는걸 방지한다.
while heap:
    w,n = heappop(heap)         #w = 시작정점에서부터 n정점까지 현재까지의  최단거리(갱신 가능성 있음) , n = 정점
    if w>cost[n]:               #w가 현재까지 알고있는 n까지의 최단거리보다 크다면 진행할 필요 없음
        continue
    for nn,ww in edge[n]:       #nn:n과 연결된 정점 , ww: n과 nn사이의 거리
        new_cost = w + ww       #new_cost : 갱신가능성이 있는 비용 = w(n까지의 최단거리) + ww(n과 nn사이의 거리)
        if new_cost<cost[nn]:   #new_cost가 cost[nn]보다 작으면 즉, 처음 방문하거나 새로운 최단거리를 찾았으면!
            cost[nn] = new_cost #cost[nn]값을 갱신해줌!
            heappush(heap,[new_cost,nn])    #nn정점의 최단거리가 갱신됐으니 nn과 이어진 다른 정점까지의 최단거리도 갱신될 수 있음. 다시 큐에 넣어줌!
print(cost[e])



