from heapq import heappush,heappop,heapify
def solution(n, k, enemy):
    if k>=len(enemy):
        return len(enemy)
    idx = 0
    sum_enemy = 0
    enemy2 = []
    while k>=0:
        if k > 0:
            while sum_enemy<=n:
                sum_enemy += enemy[idx]
                heappush(enemy2,-enemy[idx])
                idx+=1
                if idx == len(enemy):
                    return idx
                    # if sum_enemy<=n:
                    #     return idx
                    # else:
                    #     return idx-1
            pro = -(heappop(enemy2))
            sum_enemy -= pro
            k-=1
        if k == 0:
            while sum_enemy<=n:
                sum_enemy += enemy[idx]
                idx+=1
                if idx == len(enemy):
                    # return idx
                    if sum_enemy<=n:
                        return idx
                    else:
                        return idx-1
            return idx-1