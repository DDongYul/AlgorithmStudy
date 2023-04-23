# 딕셔너리 사용 -> 처음 플레이어 상태를 딕셔너리에 담음
# 딕셔너리에서 조회해서 인덱스를 찾음, 이전 인덱스를 player에서 조회하고 딕셔너리 값 바꿔줌

def solution(players, callings):
    dic = {}
    for i in range(len(players)):
        dic[players[i]] = i

    for i in callings:
        idx = dic[i]
        change = players[idx - 1]
        dic[i] = idx - 1
        dic[change] = idx
        players[idx - 1] = i
        players[idx] = change
    return players