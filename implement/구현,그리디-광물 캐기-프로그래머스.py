#https://school.programmers.co.kr/learn/courses/30/lessons/172927

def solution(picks, minerals):
    answer = 0
    temp = 0
    s = []

    minerals = minerals[0:sum(picks)*5]
    for i in range(0,len(minerals)):
        if minerals[i] == "diamond":
            temp+=25
        elif minerals[i] == "iron":
            temp+=5
        else:
            temp+=1
        if i%5 == 4 or i == len(minerals)-1:
            s.append(temp)
            temp=0

    for i in range(len(s)):
        if picks[0]:
            idx = s.index(max(s))
            for j in range(5 * idx, 5 * idx + 5):
                if j >= len(minerals):
                    break
                else:
                    answer+=1
            s[idx] = 0
            picks[0]-=1

        elif picks[1]:
            idx = s.index(max(s))
            for j in range(5*idx,5*idx+5):
                if j>=len(minerals):
                    break
                else:
                    if minerals[j] == "diamond":
                        answer+=5
                    else:
                        answer+=1
            s[idx] = 0
            picks[1] -= 1
        elif picks[2]:
            answer += sum(s)
            return answer
    return answer

picks = [0, 1, 1]
minerals = ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron","iron","diamond"]
print(solution(picks,minerals))