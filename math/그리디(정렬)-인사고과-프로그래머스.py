#https://school.programmers.co.kr/learn/courses/30/lessons/152995
def solution(scores):
    answer = 1

    target = scores[0]
    target_score = sum(scores[0])
    scores.sort(key=lambda x: (-x[0], x[1]))

    threshold = 0
    for score in scores:
        if target[0] < score[0] and target[1] < score[1]:
            return -1
        if threshold <= score[1]:
            if target_score < score[0] + score[1]:
                answer += 1
            threshold = score[1]
    return answer

#처음 생각; 가장 큰 x일때 x,y 값보다 둘다 작은거 거름, 가장 큰 y일때 x,y값보다 둘다 작은거 거름 -> 아래와 같은 반례
#10,10 / 9,15 / 6,17 -> 7,14 못거름
#