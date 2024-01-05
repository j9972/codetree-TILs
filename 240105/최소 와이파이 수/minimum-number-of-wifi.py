n,m = map(int,input().split())

arr = list(map(int,input().split()))

cnt = 0
idx  = 0

while idx < n:
    if arr[idx] == 1:
        cnt += 1
        idx +=  (2*m) + 1
    else:
        idx += 1
    
print(cnt)