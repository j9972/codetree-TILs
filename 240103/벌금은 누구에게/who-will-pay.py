n,m,k = map(int,input().split())

arr = [
    int(input())
    for _ in range(m)
]

d = [0] * (n+1)

ans = -1
for i in arr:
    d[i] += 1
    if d[i] >= k:
        ans = i
        break
print(ans)