n = int(input())
arr = list(input().split())

ans = 0
for i in range(n):
    x = chr(ord('A') + i)

    cnt = 0
    for j in range(1,n):
        if arr[j] == x:
            cnt = j
    
    for j in range(cnt-1, i-1, -1):
        arr[j],arr[j+1] = arr[j+1],arr[j]
        ans += 1
print(ans)