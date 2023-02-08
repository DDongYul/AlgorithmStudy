#K: 상자를 포장하는 비용(모든 상자에 공통값) a: 가장 큰 오렌지의 크기 b:가장 작은 오렌지의 크기 s:상자에 넣은 오렌지의 개수
import sys
input = sys.stdin.readline
N,M,K = map(int,input().split())
data = [0]
for _ in range(N):
    data.append(int(input()))

DP = [ 0 for _ in range(N+1)]
DP[1]= K

for i in range(2,N+1):
    a = b = data[i]
    DP[i] = DP[i-1] + K
    for l in range(2, min(M,i)+1):
        j = i-l +1
        a = max(a,data[j])
        b = min(b,data[j])
        cost = K+l*(a-b)
        DP[i] = min(DP[i],DP[j-1]+cost)

print(DP[N])

