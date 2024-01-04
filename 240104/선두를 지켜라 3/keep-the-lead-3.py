n,m = map(int,input().split())

d = [0] * 1000001

a_idx = 1
for i in range(n):
    v,t = tuple(map(int,input().split()))
    for _ in range(t):
        d[a_idx] = d[a_idx-1] + v
        a_idx += 1

dp = [0] * 1000001

b_idx = 1
for i in range(m):
    v,t =tuple(map(int,input().split()))
    for _ in range(t):
        dp[b_idx] = dp[b_idx-1] + v
        b_idx += 1

leader, ans = 0,0
for i in range(1,a_idx):
    if d[i] > dp[i]:
        if leader == 2 or leader == 0:
            ans += 1
        leader = 1
    elif d[i] < dp[i]:
        if leader == 1 or leader == 0:
            ans += 1
        leader = 2
    elif d[i] == dp[i]:
        if leader == 1 or leader == 2:
            ans += 1
        leader = 0
print(ans)