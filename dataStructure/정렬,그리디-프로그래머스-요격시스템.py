# from heapq import heappush,heappop,heapify
#
# ##처음 풀이 (정렬 Nlog(N)이라 크기 500,000 배열에서 시간초과 날 줄 알았음(heapify도 시간복잡도 O(NlogN)임)
# def solution(targets):
#     answer = 0
#     heapify(targets)
#     curr = 0
#     while targets:
#         x,y = heappop(targets)
#         if x>=curr:
#             answer+=1
#             curr = y
#         else:
#             if y<curr:
#                 curr = y
#             continue
#     return answer

#굳이 pop 할 필요 없이 index 사용해서 풀면 더 효율적
def solution(targets):
    answer = 0
    targets.sort(key=lambda x:(x[0],x[1]))
    curr = 0
    for i in range(len(targets)):
        x,y = targets[i]
        if x>=curr:
            answer+=1
            curr = y
        else:
            if y<curr:
                curr = y
    return answer