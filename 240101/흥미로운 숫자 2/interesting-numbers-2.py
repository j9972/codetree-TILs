x,y = map(int,input().split())

ans = 0
for i in range(x,y+1):
    tmp = dict()
    
    for j in str(i):
        if j not in tmp:
            tmp[j] = 1
        else:
            tmp[j] += 1

    if len(tmp) == 1 or len(tmp) >= 3:
        continue

    #print(tmp, len(tmp))

    cnt = 0
    for t in tmp:
        if tmp[t] != 1:
            cnt += 1

    if cnt == 1:
        ans += 1

print(ans)