import sys
input = sys.stdin.readline
from itertools import combinations

vowel = ["a","e","i","o","u"]
L,C = map(int,input().split())
voca = sorted(list(input().strip().split()))

lst = list(combinations(voca,L))
answer = []
for i in lst:
    cnt = 0
    for j in i:
        if j in vowel:
            cnt+=1
    if cnt!=0 and L-cnt>=2:
        answer.append("".join(i))
for i in answer:
    print(i)

