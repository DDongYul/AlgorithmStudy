import sys

T=int(sys.stdin.readline())
for i in range(0,T):
    line2 = list(map(int,sys.stdin.readline().split()))
    N = line2[0]
    M=line2[1]
    listA = list(map(int,sys.stdin.readline().split()))
    listB = list(map(int,sys.stdin.readline().split()))
    listA.sort()
    listB.sort()

    left=0
    right=0
    count = 0

    while left < N:
        if listA[left] <= listB[right]:
            count += right
            left+=1

        elif listA[left] > listB[right]:
            while listA[left] > listB[right]:
                if right == M-1:
                    count += right+1
                    left+=1
                    break
                right+=1
    print(count)