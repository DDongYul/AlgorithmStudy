import math


def solution(weights):
    answer = 0
    w = [0 for _ in range(1001)]
    for i in weights:
        w[i] += 1

    for i in w:
        if i>=2:
            answer+=math.comb(i,2)

    sw = sorted(weights)
    mask = [0 for _ in range(1001)]

    for i in range(len(sw)):
        curr = sw[i]
        if mask[curr]:
            answer+=mask[curr]
            continue
        else:
            c1=(curr*3)/2
            c2=(curr*4)/2
            c3=(curr*4)/3
            if curr*3 % 2 == 0 and 100<=c1<=1000:
                mask[curr]+= w[int(c1)]
            if curr*4 % 2 == 0 and 100<=c2<=1000:
                mask[curr]+= w[int(c2)]
            if curr*4 % 3 == 0 and 100<=c3<=1000:
                mask[curr]+= w[int(c3)]
            answer+= mask[curr]

    return answer