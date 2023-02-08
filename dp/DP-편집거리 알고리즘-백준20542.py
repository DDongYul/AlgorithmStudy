# 승연 v -> v,w모두 가능
# 승연 i -> i,j,l 모두 가능
#추가 , 삭제 , 변환 모두 비용 1
#편집거리 알고리즘 -> D[i,j] = min(D[i,j-1] + 삽입 비용, D[i-1,j] + 삭제비용, D[i-1,j-1] + 대치 비용)
#대치 비용은 S[i] == T[j] 일 때는 0, S[i] != T[j]일 때는 1   (참고 S: 원래 스트링  T: 비교 스트링)

n,m = map(int,input().split())
S1 = input()
S2 = input()
DP = [[0 for _ in range(n+1)] for _ in range(m+1)]
for i in range(n+1):
    DP[0][i] = i
for j in range(m+1):
    DP[j][0] = j

for i in range(1,m+1):
    for j in range(1,n+1):
        T=1
        s = S1[j-1]
        a = S2[i-1]
        if s == a:
            T=0
        elif s == 'v' and a == 'w':
            T=0
        elif s == 'i' and (a == 'j' or a== 'l'):
            T=0
        DP[i][j] = min(DP[i-1][j]+1,DP[i][j-1]+1,DP[i-1][j-1]+T)    #각각 삽입,삭제,대치 순

print(DP[m][n])