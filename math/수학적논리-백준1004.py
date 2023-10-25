#출발점과 도착점이 어떤 원의 경계 안에 있는지만 검사하면 됨!
#거리로 비교하면 될듯. 중점에서 점과 거리 <= 반지름이면 속해있음
import sys
input = sys.stdin.readline

def check(x1,y1,x2,y2,r):
    d = pow(abs(x1-x2),2) + pow(abs(y1-y2),2)
    if d<= pow(r,2):
        return True;
    return False;

T = int(input())
for _ in range(T):
    x1,y1,x2,y2 = map(int,input().split())
    n = int(input())
    answer = 0
    for _ in range(n):
        cx,cy,cr = map(int,input().split())
        if check(x1,y1,cx,cy,cr) and not check(x2,y2,cx,cy,cr):
            answer+=1
        if check(x2,y2,cx,cy,cr) and not check(x1,y1,cx,cy,cr):
            answer+=1
    print(answer)
