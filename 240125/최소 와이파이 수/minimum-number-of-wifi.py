n,m = map(int,input().split())
arr = list(map(int,input().split()))

wifi = 0
idx = 0
while idx < n:
    if idx + 2 * m >= n:
        break
    
    if sum(arr[idx:idx+2*m]) >= 1:
        wifi += 1
        idx += 2 * m
    else:
        idx += 1
print(wifi)