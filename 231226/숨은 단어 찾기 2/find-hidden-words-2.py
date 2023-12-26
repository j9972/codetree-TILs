r,c = map(int,input().split())
arr = [
    list(input())
    for _ in range(r)
]

cnt = 0

# 가로
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'L':
            if (j >= 2) and (arr[i][j-2] == 'E' and arr[i][j-1] == 'E'):
                cnt += 1
            if (j <= c-3) and (arr[i][j+1] == 'E' and arr[i][j+2] == 'E'):
                cnt += 1

# 세로
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'L':
            if (i >= 2) and (arr[i-2][j] == 'E' and arr[i-1][j] == 'E'):
                cnt += 1
            if (i <= r-3) and (arr[i+1][j] == 'E' and arr[i+2][j] == 'E'):
                cnt += 1

# 대각
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'L':
            if (i >= 2) and (j >= 2) and (arr[i-1][j-1] == 'E' and arr[i-2][j-2] == 'E'):
                cnt += 1
            if (i >= 2) and (j <= c-3) and (arr[i-1][j+1] == 'E' and arr[i-2][j+2] == 'E'):
                cnt += 1
            if (i <= r-3) and (j >= 2) and (arr[i+1][j-1] == 'E' and arr[i+2][j-2] == 'E'):
                cnt += 1
            if (i <= r-3) and (j <= c-3) and (arr[i+1][j+1] == 'E' and arr[i+2][j+2] == 'E'):
                cnt += 1
print(cnt)