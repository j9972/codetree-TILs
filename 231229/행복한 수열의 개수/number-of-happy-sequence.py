n,m = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

ans = 0

def happy(new):
    seq,cnt = 1,1
    for i in range(1,n):
        if new[i-1] == new[i]:
            seq += 1
        else:
            seq = 1
        cnt = max(cnt, seq)
    return cnt >= m

# 가로
for i in range(n):
    new = arr[i][:]
    if happy(new):
        ans += 1

# 세로
for i in range(n):
    new = list()
    for j in range(n):
        new.append(arr[j][i])
    if happy(new):
        ans += 1
print(ans)