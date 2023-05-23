from heapq import heappush,heappop

#이번에 작업할 걸 뽑는 함수
def filter(n,lst):
    rst = []
    for t,w in lst:
        if t<=n:
            heappush(rst,(w,t))
        else:
            break
    if not rst:
        return (0,0)
    return heappop(rst)

def solution(jobs):
    answer = 0
    n = len(jobs)
    cnt = 0
    jobs.sort()
    while jobs:
        w,t = filter(cnt,jobs)
        if w==0 and t==0:
            cnt+=1
            continue
        cnt += w
        answer += (cnt-t)
        jobs.pop(jobs.index([t,w]))
    return answer // n