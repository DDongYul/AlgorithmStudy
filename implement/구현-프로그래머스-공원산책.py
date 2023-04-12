def solution(park, routes):
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                curr = [i, j]

    for route in routes:
        op = route[0]
        n = int(route[2:])
        if op == "N":
            flag = True
            if curr[0] - n < 0:
                continue
            for i in range(curr[0], curr[0] - n-1,-1):
                if park[i][curr[1]] == "X":
                    flag = False
                    break
            if flag:
                curr = [curr[0] - n, curr[1]]
            else:
                continue

        elif op == "S":
            flag = True
            if curr[0] + n >= len(park):
                continue
            for i in range(curr[0], curr[0] + n+1):
                if park[i][curr[1]] == 'X':
                    flag = False
                    break
            if flag:
                curr = [curr[0] + n, curr[1]]
            else:
                continue

        elif op == "E":
            flag = True
            if curr[1] + n >= len(park[0]):
                continue
            for i in range(curr[1], curr[1] + n+1):
                if park[curr[0]][i] == "X":
                    flag = False
                    break
            if flag:
                curr = [curr[0], curr[1] + n]
            else:
                continue

        elif op == "W":
            flag = True
            if curr[1] - n < 0:
                continue
            for i in range(curr[1], curr[1] - n-1,-1):
                if park[curr[0]][i] == "X":
                    flag = False
                    break
            if flag:
                curr = [curr[0], curr[1] - n]
            else:
                continue
    return curr
