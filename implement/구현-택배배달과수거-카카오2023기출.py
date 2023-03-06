def solution(cap, n, deliveries, pickups):
    answer = 0
    deliveries = list(reversed(deliveries))
    pickups = list(reversed(pickups))
    curr_del = 0
    curr_pic = 0
    td = 0
    tp = 0
    while True:
        if curr_del>=n and curr_pic>=n:
            break

        if curr_del<n:
            while deliveries[curr_del] == 0:
                curr_del+=1
                if curr_del>=n:
                    break
        if curr_pic<n:
            while pickups[curr_pic] == 0:
                curr_pic+=1
                if curr_pic>=n:
                    break
        answer+= max(n-curr_pic,n-curr_del)*2

        if curr_del<n:
            while td<cap:
                if td+deliveries[curr_del]>=cap:
                    deliveries[curr_del]-=(cap-td)
                    td = cap
                else:
                    td+=deliveries[curr_del]
                    deliveries[curr_del]=0
                    curr_del+=1
                    if curr_del >= n:
                        break
        if curr_pic<n:
            while tp<cap:
                if tp+pickups[curr_pic]>=cap:
                    pickups[curr_pic]-=(cap-tp)
                    tp = cap
                else:
                    tp+=pickups[curr_pic]
                    pickups[curr_pic]=0
                    curr_pic+=1
                    if curr_pic >= n:
                        break
        td = 0
        tp = 0
    return answer

c=2
nn=7
d=[1, 0, 2, 0, 1, 0, 2]
p=[0, 2, 0, 1, 0, 2, 0]
print(solution(c,nn,d,p))



