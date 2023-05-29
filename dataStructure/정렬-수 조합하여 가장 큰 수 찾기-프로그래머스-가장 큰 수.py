def solution(numbers):
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])
    numbers.sort(key = lambda x:x*3,reverse = True)
    if numbers[0] == '0':
        return '0'
    return ''.join(numbers)