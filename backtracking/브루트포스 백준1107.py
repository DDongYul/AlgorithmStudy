N = input()             #구현의 편의를 위해 문자열로 받음
M = int(input())
button = [True]*10
if M != 0:
    broken_button = list(map(int,input().split()))
    for i in broken_button:
        button[i] = False

if M == 10:             #모두 고장났으면 +,-로 밖에 못 움직임
    print(abs(int(N)-100))
else:
    flag = True
    left = N
    right = N

    while flag:
        flag2 = True        #flag2는 해당 채널의 모든 번호가 고장나지 않았을때만 True
        for i in left:
            i = int(i)
            if not button[i]:
                flag2 = False
                break
        if flag2:
            temp = int(left)    #채널이동이 가능한 N과 가장 가까운 채널 번호
            flag = False
        else:
            if int(left) > 0:
                left = str(int(left)-1)

        if flag:            #만약 left에서 결과가 나왔으면 left가 무조건 작거나 같기떄문에 left의 결과를 반영해줘야함 아래 반례
            flag3 = True
            for i in right:
                i = int(i)
                if not button[i]:
                    flag3 = False
                    break
            if flag3:
                temp = int(right)
                flag = False
            else:
                right = str(int(right)+1)

    result = min(abs(int(N)-100) , abs(int(N)-temp)+len(str(temp)))     #버튼을 눌러 이동한 경우와 100번에서 +,-로만 이동한것중 작은 것이 답
    print(result)

# 944
# 8
# 0 2 3 4 5 6 8 9
# 777 1111 (left,right) -> 둘 다 944채널까지의 거리가 같지만 777은 3번만 누르면 됨
# 170
