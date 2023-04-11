def solution(sequence, k):
    answer = []
    dx = 0
    dy = 0
    flag = True

    temp = sequence[0]  # 부분합

    if temp == k:
        return [0, 0]  # 처음값이 k면 [0,0]리턴

    while flag:
        while temp <= k:
            dy += 1
            if dy >= len(sequence):
                flag = False
                break
            temp += sequence[dy]
            if temp == k:
                answer.append((dx, dy, dy - dx))

        while temp >= k:
            temp -= sequence[dx]
            dx += 1
            if dx > dy:
                break
            if temp == k:
                answer.append((dx, dy, dy - dx))

    answer = sorted(answer, key=lambda x: (x[2], x[0]))  # 1.구간 짧은 순, 첫 인덱스 작은순
    answer = answer[0][0:2]
    return answer