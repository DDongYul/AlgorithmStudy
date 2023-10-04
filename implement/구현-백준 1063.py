import sys
input = sys.stdin.readline

graph = [[0 for _ in range(8)] for _ in range(8)]
row = ['A','B','C','D','E','F','G','H']
move = {'R':(0,1), 'L':(0,-1), 'B':(-1,0), 'T':(1,0), 'RT':(1,1), 'LT':(1,-1), 'RB':(-1,1), 'LB':(-1,-1)}

K,R,N = input().strip().split()
curr_K = [int(K[1])-1,row.index(K[0])]  #행,열
curr_R = [int(R[1])-1,row.index(R[0])]

for _ in range(int(N)):
    m = input().strip()
    d = move[m]
    if (0<= curr_K[0] + d[0] <8) and (0<=curr_K[1] + d[1] <8):
        if curr_K[0]+d[0] == curr_R[0] and curr_K[1]+d[1] == curr_R[1]:
            if (0 <= curr_R[0] + d[0] < 8) and (0 <= curr_R[1] + d[1] < 8):
                curr_R[0] += d[0]
                curr_R[1] += d[1]
            else:
                continue
        curr_K[0] += d[0]
        curr_K[1] += d[1]

k_col = str(curr_K[0]+1)
k_row = row[curr_K[1]]
r_col = str(curr_R[0]+1)
r_row = row[curr_R[1]]
print(k_row+k_col)
print(r_row+r_col)