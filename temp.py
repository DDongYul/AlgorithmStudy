def solution(picks, minerals):
    answer = 0

    if len(minerals) % 5 == 0:
        need = len(minerals)//5
    else:
        need = len(minerals)//5 + 1

    temp = 0
    s = []
    if sum(picks) >= need:   #곡괭이가 층분할 때
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
    else:
        for i in range(0,sum(picks)*5):
            if minerals[i] == "diamond":
                temp+=25
            elif minerals[i] == "iron":
                temp+=5
            else:
                temp+=1
            if i % 5 == 4 or i == len(minerals) - 1:
                s.append(temp)
                temp = 0


    for i in range(len(s)):
        print(s)
        if picks[0]:
            answer += 5
            s[s.index(max(s))]=0
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
            idx = s.index(max(s))
            # for j in range(5 * idx, 5 * idx + 5):
            #     if j >= len(minerals):
            #         break
            #     else:
            #         if minerals[j] == "diamond":
            #             answer += 25
            #         elif minerals[j] == "iron":
            #             answer += 5
            #         else:
            #             answer+=1
            answer+=max(s)
            s[idx] = 0
            picks[2] -= 1
        print("answer", answer)
        print("picks", picks)

    return answer

picks = [1, 1, 1]
minerals = ["diamond", "diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "diamond","iron","diamond"]
print(solution(picks,minerals))