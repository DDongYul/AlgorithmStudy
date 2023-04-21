# 한번 누르면 되는거 리스트, 두번 리스트 ... n번 리스트
# 리스트 돌면서 있으면 리스트 index+1 더하고 없으면 넘김
def solution(keymap, targets):
    answer = []
    lst = [[] for _ in range(101)]
    for key in keymap:
        for j in range(len(key)):
            lst[j + 1].append(key[j])

    for target in targets:
        temp = 0
        for t in target:
            for idx, c in enumerate(lst):
                flag = False
                if t in c:
                    temp += idx
                    flag = True
                    break
            if not flag:
                temp = -1
                break
        if temp == -1:
            answer.append(-1)
        else:
            answer.append(temp)

    return answer