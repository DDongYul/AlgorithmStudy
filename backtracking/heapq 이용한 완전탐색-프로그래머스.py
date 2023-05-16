#조건: 한 턴마다 한개의 단어만 바꿀 수 있고, words안에 있는 단어로 바꿔야한다.
#words안에 target 없으면 0
#heapq로 (횟수,알파벳) 해서 최소거리 계산

def diff(word1,word2):
    cnt = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            cnt+=1
    return cnt

def sol(word,words):
    rst = []
    for i in words:
        cnt = diff(word,i)
        if cnt == 1:
            rst.append(i)
    return rst

from heapq import heappush,heappop
INF = int(1e10)
def solution(begin, target, words):
    if target not in words:
        return 0
    dist = [INF for _ in range(len(words))]
    heap = [(0,begin)]
    while heap:
        w,curr = heappop(heap)
        rst = sol(curr,words)
        for i in rst:
            ww = dist[words.index(i)]
            if ww>w+1:
                dist[words.index(i)] = w+1
                heappush(heap,(w+1,i))
    return dist[words.index(target)]