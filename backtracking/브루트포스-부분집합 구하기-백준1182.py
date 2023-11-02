import sys
input = sys.stdin.readline

N,S = map(int,input().split())
lst = list(map(int,input().split()))

answer = 0

##재귀를 이용한 방법##
def sol(depth,curr):
    global answer
    if depth == N:
        if curr == S:
            answer += 1
        return
    sol(depth+1,curr+lst[depth])
    sol(depth+1,curr)

sol(0,0)
##공집합 빼주기
if S==0:
    answer-=1
print(answer)

##비트맵을 이용한 방법##
for i in range(1,pow(2,N)):
    curr = 0
    bit = bin(i)[2:]
    for j in range(0, len(bit)):
        if bit[j] == '1':
            curr+=lst[len(bit)-j-1]
    if curr == S:
        answer+=1

print(answer)
