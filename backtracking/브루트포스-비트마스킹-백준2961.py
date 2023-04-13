import sys
N = int(sys.stdin.readline())
data = []
for _ in range(0,N):
    a,b = map(int,sys.stdin.readline().split())
    data.append((a,b))

result = []
for i in range(1,pow(2,N)):
    taste1 = 1
    taste2 = 0
    bit = bin(i)[2:]
    for j in range(0,len(bit)):
        if bit[j] == '1':
            taste1*=data[len(bit)-j-1][0]
            taste2+=data[len(bit)-j-1][1]
    result.append(abs(taste2-taste1))

print(min(result))