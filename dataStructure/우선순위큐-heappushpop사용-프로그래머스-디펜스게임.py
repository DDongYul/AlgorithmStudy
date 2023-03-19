# https://school.programmers.co.kr/learn/courses/30/lessons/142085

#내풀이
from heapq import heappush,heappop,heapify,heappushpop
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
            pro = -(heappop(enemy2))
            sum_enemy -= pro
            k-=1
        if k == 0:
            while sum_enemy<=n:
                sum_enemy += enemy[idx]
                idx+=1
                if idx == len(enemy):
                    if sum_enemy<=n:
                        return idx
                    else:
                        return idx-1
            return idx-1

#heappushpop을 사용한 간단한 풀이 -> 우선순위가 낮은 값(큰 값)을 모아두는 우선순위 큐
#heappushpop(q,enemy[idx]) q에는 우선순위가 낮은 값(더 큰 값)들이 저장됨
import heapq as hq
def solution2(n, k, enemy):
    q = enemy[:k]
    hq.heapify(q)
    for idx in range(k,len(enemy)):
        n -= hq.heappushpop(q,enemy[idx])
        print(n)
        if n < 0:
            return idx
    return len(enemy)

solution2(7,3,[4, 2, 4, 5, 3, 3, 1])
