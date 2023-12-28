n,m = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

cnt = 0

# 가로
for i in range(n):
    f = False
    for j in range(n-m+1):
        for _ in range(m-1):
            if arr[i][j] != arr[i][j+1]:
                break
            cnt += 1
            f = True
        if f:
            break

for j in range(n):
    f = False
    for i in range(n-m+1):
        for _ in range(m-1):
            if arr[i][j] != arr[i+1][j]:
                break
            cnt += 1
            f = True
        if f:
            break

print(cnt)