from itertools import product

def solution(users, emoticons):
    answer = []
    eplus = 0
    total = 0

    for case in product([10,20,30,40], repeat=len(emoticons)):
        for rate, price in users:
            tp = 0
            for idx, r in enumerate(case):
                if rate <= r:
                    tp += int((emoticons[idx] * (100 - r) / 100))
            if tp >= price:
                eplus += 1
            else:
                total += tp
        answer.append((eplus, total))
        eplus = 0
        total = 0

    return max(answer)

#u = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
#e = [1300, 1500, 1600, 4900]