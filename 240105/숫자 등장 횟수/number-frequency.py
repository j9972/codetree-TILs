n,m = map(int,input().split())
n_arr = list(map(int,input().split()))
m_arr = list(map(int,input().split()))

res = []
for mm in m_arr:
    cnt = 0
    for nn in n_arr:
        if mm == nn:
            cnt += 1
    
    res.append(cnt)

for i in res:
    print(i, end=' ')