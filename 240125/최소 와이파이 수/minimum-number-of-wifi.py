n,m = map(int,input().split())
arr = list(map(int,input().split()))

wifi = 0
idx = 0
while idx < n:
    if idx + 2 * m >= n:
        break
    
    for i in range(idx, idx + 2 * m):
        if arr[i] == 1:
            wifi += 1
            break
    idx += 2 * m
print(wifi)