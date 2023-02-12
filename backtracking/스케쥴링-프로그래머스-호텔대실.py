from heapq import heappush, heappop

def solution(book_time):
    answer = 1
    lst = []
    for i in book_time:
        start_hour = int(i[0][0:2])
        start_min = int(i[0][3:5])
        end_hour = int(i[1][0:2])
        end_min = int(i[1][3:5])
        lst.append((start_hour * 60 + start_min, end_hour * 60 + end_min))
        
    lst.sort()
    heap = []
    for s, e in lst:
        if not heap:
            heappush(heap, e)
            continue
        if heap[0] <= s:
            heappop(heap)
        else:
            answer += 1
        heappush(heap, e + 10)

    return answer