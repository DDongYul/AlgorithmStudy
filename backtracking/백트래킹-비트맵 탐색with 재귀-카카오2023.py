def sol(num):
    if len(num) == 1:
        return True
    center = len(num) // 2
    if num[center] == '1':
        flag1 = sol(num[0:center])
        flag2 = sol(num[center + 1:])
        if flag1 and flag2:
            return True
        return False
    else:
        for i in num:
            if i == '1':
                return False
        return True

def solution(numbers):
    answer = []
    for i in numbers:
        if i == 0:
            answer.append(0)
            continue
        if i == 1:
            answer.append(1)
            continue
        number = bin(i)[2:]
        for j in range(1, len(number)+1):
            c = pow(2, j) - 1
            if c >= len(number):
                while len(number) < c:
                    number = '0' + number
                break
        flag = sol(number)
        if flag:
            answer.append(1)
        else:
            answer.append(0)
    return answer

case = [0,1,2,3,4,5]
print(solution(case))