def solution(name, yearning, photo):
    answer = []
    dic = {}
    for i in range(len(name)):
        dic[name[i]] = yearning[i]

    for i in photo:
        temp = 0
        for j in i:
            if j in dic:
                temp += dic[j]
        answer.append(temp)

    return answer