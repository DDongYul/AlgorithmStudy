# 사전 순
from itertools import product

def solution(word):
    vowel = ['A', 'E', 'I', 'O', 'U']
    words = []
    for i in range(1, 6):
        temp = list(product(vowel, repeat=i))
        for j in temp:
            words.append(''.join(j))
    words.sort()
    return words.index(word) + 1
