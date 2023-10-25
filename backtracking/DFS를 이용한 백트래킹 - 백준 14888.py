import sys
input = sys.stdin.readline
INF = sys.maxsize

def sol(depth, curr, plus, minus, multiply, divide):
    if depth == N-1:
        max_answer[0] = max(curr,max_answer[0])
        min_answer[0] = min(curr,min_answer[0])
        return
    if plus:
        sol(depth+1, curr+num[depth+1], plus-1, minus, multiply, divide)
    if minus:
        sol(depth+1, curr-num[depth+1], plus, minus-1, multiply, divide)
    if multiply:
        sol(depth+1, curr*num[depth+1], plus, minus, multiply-1, divide)
    if divide:
        sol(depth+1, int(curr/num[depth+1]), plus, minus, multiply, divide-1)

N = int(input())
num = list(map(int,input().split()))
a,b,c,d = map(int,input().split())
max_answer = [-INF]
min_answer = [INF]

sol(0,num[0], a, b, c, d)
print(max_answer[0])
print(min_answer[0])





