def solution(numbers, target):
    answer = 0
    n = len(numbers)
    for i in range(pow(2, n)):
        bitmap = bin(i)[2:]
        while len(bitmap) < n:
            bitmap = '0' + bitmap
        temp = 0
        for j in range(n):
            if bitmap[j] == '0':
                temp -= numbers[j]
            else:
                temp += numbers[j]
        if temp == target:
            answer += 1
    return answer
