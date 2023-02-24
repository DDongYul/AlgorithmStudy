def solution(numbers):
    n = len(numbers)
    answer = [-1 for _ in range(n)]
    stack = [(numbers[0], 0)]
    for i in range(1, n):
        for j in range(len(stack)):
            if stack[-1][0] < numbers[i]:
                curr = stack.pop()
                answer[curr[1]] = numbers[i]
            else:
                break
        stack.append((numbers[i], i))

    return answer

# a = [9,1,5,3,6,2]
# solution(a)