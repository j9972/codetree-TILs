n = int(input())
a = [
    int(input())
    for _ in range(n)
]
max_val = 0
cnt = 1
for i in range(1,n):
    if a[i] != a[i-1]:
        max_val = max(max_val, cnt)
        cnt = 1
    else:
        cnt += 1

print(max_val)