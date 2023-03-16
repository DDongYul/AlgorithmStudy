#https://school.programmers.co.kr/learn/courses/30/lessons/140107
def solution(k, d):
    answer = 0
    mok = d // k
    dd = d * d
    squ = [(i * k) * (i * k) for i in range(mok + 1)]
    y = len(squ) - 1
    for x in range(len(squ)):
        while squ[x] + squ[y] > dd:
            y -= 1
            if y < 0:
                break
        answer += (y + 1)

    return answer