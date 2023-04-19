#시작점에서 가로,세로 첫번째 지점이 시작, 끝점에서 가로, 세로 첫번째 지점이 끝점
def solution(wallpaper):
    lux = 50
    luy = 50
    rdx=0
    rdy=0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                lux = min(lux,i)
                luy = min(luy,j)
                rdx = max(rdx,i+1)
                rdy = max(rdy,j+1)
    answer = [lux,luy,rdx,rdy]
    return answer