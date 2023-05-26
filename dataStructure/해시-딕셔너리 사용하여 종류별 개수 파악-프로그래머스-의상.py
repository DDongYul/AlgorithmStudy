def solution(clothes):
    answer = 1
    dic = {}
    for a,b in clothes:
        if b in dic:
            dic[b].append(a)
        else:
            dic[b] = [a]    #값 여러개 넣기 위해 배열로 선언 key:value 에서 value값을 배열!
    for i in dic.keys():
        temp = len(dic[i])+1
        answer*=temp
    return answer-1