def solution(brown, yellow):
    answer = []
    cnt = brown+yellow
    for w in range(1,cnt+1):
        for y in range(1,cnt+1):
            temp = w*y
            if temp == cnt:
                if (2*w + 2*y -4) == brown and ((w-2)*(y-2) == yellow):
                    return[y,w]
            elif temp<cnt:
                continue
            elif temp>cnt:
                break
    return answer