n = int(input())
a = [
    int(input())
    for _ in range(n)
]

ans, cnt = 0, 0
for i in range(n):
    if i == 0 or a[i - 1] < a[i]:
        cnt += 1
    else:
        cnt = 1
    ans = max(ans, cnt)

print(ans)