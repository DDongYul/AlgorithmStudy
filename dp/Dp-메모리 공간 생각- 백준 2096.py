import sys
input = sys.stdin.readline

n = int(input())
dp1 = []
dp2 = []

#그냥 temp값을 dp1,dp2에 넣으면 temp 리스트를 추가할 때 참조하는 객체가 동일하기 때문에 같은 리스트가 됨
#즉 dp1을 바꾸면 dp2도 값이 바뀜, 이런식으로 복사한 list를 넣어줘야한다.
for _ in range(n):
    temp = list(map(int,input().split()))
    dp1.append(temp[:])
    dp2.append(temp[:])

for i in range(1,n):
    dp1[i][0] = max(dp1[i-1][0],dp1[i-1][1]) + dp1[i][0]
    dp1[i][1] = max(dp1[i-1][0],dp1[i-1][1],dp1[i-1][2]) + dp1[i][1]
    dp1[i][2] = max(dp1[i-1][1],dp1[i-1][2]) + dp1[i][2]

    dp2[i][0] = min(dp2[i - 1][0], dp2[i - 1][1]) + dp2[i][0]
    dp2[i][1] = min(dp2[i - 1][0], dp2[i - 1][1], dp2[i - 1][2]) + dp2[i][1]
    dp2[i][2] = min(dp2[i - 1][1], dp2[i - 1][2]) + dp2[i][2]

print(max(dp1[n-1]) , min(dp2[n-1]))