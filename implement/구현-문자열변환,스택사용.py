#https://school.programmers.co.kr/learn/courses/30/lessons/176962
def solution(plans):
    for i in range(len(plans)):
        start = plans[i][1]
        sp = list(start.split(":"))
        minute = int(sp[0]) * 60 + int(sp[1])
        plans[i][1] = minute
        plans[i][2] = int(plans[i][2])

    plans = sorted(plans, key=lambda x: x[1])
    plans.append(['temp',100000,0]) #마지막과제 끝내기 위한 더미데이터
    result = []
    pause = []
    for i in range(len(plans) - 1):
        pt = plans[i + 1][1] - plans[i][1]  # 일 가능한 시간
        if pt >= plans[i][2]:   #일 가능한시간 > 다음 과제까지 시간
            result.append(plans[i][0])  # 일 종료
            rt = pt - plans[i][2]
            while pause and rt:
                name,playtime = pause.pop()
                if playtime > rt:   #중단한 잔여 작업이 남는 시간보다 많음
                    playtime -= rt
                    pause.append([name,playtime])
                    break
                else:
                    result.append(name)
                    rt -= playtime
        else:
            pause.append([plans[i][0], plans[i][2] - pt])
    if pause:
        name, playtime = pause.pop()
        result.append(name)

    return result

plan = [["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]
print(solution(plan))