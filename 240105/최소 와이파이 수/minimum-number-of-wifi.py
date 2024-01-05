n,m = map(int,input().split())

arr = list(map(int,input().split()))

cnt = 0
idx  = 0

while idx <= n:
    if arr[idx] == 1:
        for j in range(idx+1,n):
            if abs(j-idx) == m:
                cnt += 1
                idx += j + 1
                break
            if j == n-1:
                cnt += 1
                break
        #print(idx , cnt)
    else:
        idx += 1
    
print(cnt)