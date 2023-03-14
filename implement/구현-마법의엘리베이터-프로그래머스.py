#https://school.programmers.co.kr/learn/courses/30/lessons/148653
def solution(storey):
    answer = 0
    while storey:
        rem = storey%10
        if rem < 5:
            answer+=rem
        elif rem > 5:
            answer+=(10-rem)
            storey+=10
        else:
            if int(storey/10)%10>=5:
                answer+=(10-rem)
                storey+=10
            elif int(storey/10)%10<5:
                answer+=rem
        storey=int(storey/10)
    return answer
