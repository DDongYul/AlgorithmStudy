import sys
input = sys.stdin.readline

N,S = map(int,input().split())
lst = list(map(int,input().split()))

answer = 0
def sol(depth,curr):
    global answer
    if depth == N:
        if curr == S:
            answer += 1
        return
    sol(depth+1,curr+lst[depth])
    sol(depth+1,curr)

sol(0,0)
if S==0:
    answer-=1
print(answer)


##비트맵 쓰는 방법 (재귀가 나은듯)

# answer = 0
# bit_len = N
# for i in range(1,int(pow(2,N))):
#     curr = 0
#     bit = bin(i)[2:]
#     while len(bit)<bit_len:
#         bit = '0' + bit
#     for j in range(bit_len):
#         if bit[j] == '1':
#             curr+=lst[j]
#     if curr == S:
#         answer+=1
#
# print(answer)
