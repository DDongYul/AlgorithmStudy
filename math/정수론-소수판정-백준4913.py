
prime = [1 for i in range(1000001)]
prime[0] =0
prime[1] = 0
# square = [0 for i in range(1000001)]

def sol():
    for i in range(2,1001):
        if prime[i] == 1:
            temp = i+i
            while temp<=1000000:
                prime[temp] = 0
                temp+=i
    # for i in range(5,1000001,4):
    #     square[i] = 1
sol()
while 1:
    L,U = map(int,input().split())
    if L==-1 and U==-1:
        break
    cnt_p=0
    cnt_s=0
    if L<0 and U>=0:
        for i in range(0,U+1):
            if prime[i]:
                cnt_p += 1
                if i%4==1:
                    cnt_s += 1
    elif L>=0 and U>=0:
        for i in range(L,U+1):
            if prime[i]:
                cnt_p+=1
                if i%4==1:
                    cnt_s+=1
    print(L,U,cnt_p,cnt_s)