r,c = map(int,input().split())
arr = [
    list(input().split())
    for _ in range(r)
]

cnt = 0

standard = arr[0][0]

for i in range(1,r-1):
    for j in range(1,c-1):
        if arr[i][j] != standard:
            for a in range(i+1,r-1):
                for b in range(j+1,c-1):
                    if arr[a][b] == standard:
                        cnt += 1
print(cnt)