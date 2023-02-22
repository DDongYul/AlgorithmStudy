#백준 13305번
#https://www.acmicpc.net/problem/13305
#핵심아이디어: 다음 도시가 현재 도시보다 기름값이 싸면 low_cost를 현재 도시의 기름값으로 바꾸고 , 아닐 시 그대로 진행

N = int(input()) #도시 개수
second_input = input()
length = second_input.split(" ")        #도시 사이 거리
third_input = input()
cost = third_input.split(" ")           #기름값
for i in range(0,N-1):
    length[i] = int(length[i])
for i in range(0,N):
    cost[i] = int(cost[i])

low_cost = cost[0]
index = 1
result = 0
while index<N:
    result += low_cost * length[index - 1]
    if low_cost>cost[index]:
        low_cost = cost[index]
    index+=1

print(result)


