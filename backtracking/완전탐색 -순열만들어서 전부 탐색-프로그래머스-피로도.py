from itertools import permutations

def sol(k,dungeon):
    cnt = 0
    for a,b in dungeon:
        if k<a:
            break
        else:
            k-=b
            cnt+=1
    return cnt

def solution(k, dungeons):
    answer = -1
    lst = list(permutations(dungeons,len(dungeons)))
    for i in lst:
        answer = max(answer,sol(k,i))
    return answer