#https://school.programmers.co.kr/learn/courses/30/lessons/138476
from collections import Counter

def solution(k, tangerine):
    answer = 0
    counter = Counter(tangerine)
    rst = sorted(list(counter.values()), reverse=True)

    for i in rst:
        k -= i
        answer += 1
        if k <= 0:
            break
    return answer

