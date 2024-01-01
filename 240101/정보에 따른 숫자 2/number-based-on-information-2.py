t,a,b = map(int,input().split())

d = [0] * 1001

for _ in range(t):
    alpha , idx = input().split()
    if alpha == 'S':
        d[int(idx)] = 1
    else:
        d[int(idx)] = 2

ans = 0

for i in range(a,b+1):
    s_length, n_length = 1001,1001
    # 미만
    for j in range(i):
        if d[j] == 1:
            s_length = min(s_length, abs(i-j))
        elif d[j] == 2:
            n_length = min(n_length, abs(i-j))

    # 이후
    for j in range(i,1001):
        if d[j] == 1:
            s_length = min(s_length, abs(i-j))
        elif d[j] == 2:
            n_length = min(n_length, abs(i-j))  
    
    if s_length <= n_length:
        ans += 1
print(ans)