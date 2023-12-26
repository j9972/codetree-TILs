r,c = map(int,input().split())
arr = [
    list(input().split())
    for _ in range(r)
]

cnt = 0

standard = arr[0][0]

if standard == arr[r-1][c-1]:
    print(0)
else:
    for i in range(1,r-1):
        for j in range(1,c-1):
            if arr[i][j] != standard:
                for a in range(i,r-1):
                    for b in range(j,c-1):
                        if arr[a][b] == standard:
                            cnt += 1
    print(cnt)