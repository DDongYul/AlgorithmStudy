from heapq import heappush,heappop

N,K = map(int,input().split())
heap = []
heappush(heap,[0,N])
inf = 100005
dp = [inf]*100001
dp[N] = 0

NN = N
count = 0
while NN >=0:
    dp[NN] = count
    heappush(heap,[dp[NN],NN])
    count+=1
    NN-=1


while heap:
    w,n = heappop(heap)
    for i in [n-1,n+1,n*2]:
        if 0<= i <= 100000:
            if i == n*2 and dp[i] == inf:
                dp[i] = w
                heappush(heap,[dp[i],i])
            elif dp[i] > w+1:
                dp[i] = w+1
                heappush(heap,[dp[i],i])

print(dp[K])