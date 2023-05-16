# 완탐 가로 10개 세로 10개 총 20개 20c1 20c2 20c3 ... 20c20 다 해봐야한다! 2^20 가지 1000* 1000
# 비트맵을 각각 선언
import copy

def reverse_w(n, graph):
    for i in range(len(graph[n])):
        if graph[n][i] == 0:
            graph[n][i] = 1
        else:
            graph[n][i] = 0


def reverse_l(n, graph):
    for i in range(len(graph)):
        if graph[i][n] == 0:
            graph[i][n] = 1
        else:
            graph[i][n] = 0


def solution(beginning, target):
    answer = 0
    rst = []
    n = len(beginning)  # 가로
    m = len(beginning[0])  # 세로
    for i in range(1, pow(2, m)):
        answer = 0
        temp = copy.deepcopy(beginning)
        bit_w = bin(i)[2:]
        while len(bit_w) < m:
            bit_w = '0' + bit_w
        for bit in range(len(bit_w)):
            if bit_w[bit] == '1':
                reverse_w(bit, temp)
                answer += 1
        for j in range(1, pow(2, n)):
            answer2 = answer
            temp2 = copy.deepcopy(temp)
            bit_l = bin(j)[2:]
            while len(bit_l) < n:
                bit_l = '0' + bit_l
            for bitt in range(len(bit_l)):
                if bit_l[bitt] == '1':
                    reverse_l(bitt, temp)
                    answer2 += 1

            flag = True
            for k in range(len(temp2)):
                for l in range(len(temp2[0])):
                    if temp2[k][l] != target[k][l]:
                        flag = False
            if flag:
                rst.append(answer2)

    if rst:
        return min(rst)
    else:
        return -1