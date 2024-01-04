n = int(input())
arr = [0] + list(input().split())
ans = 0

for i in range(1,n+1):
    x = chr(ord('A') + i - 1 )

    idx = 0
    for j in range(1,n+1):
        if arr[j] == x:
            idx = j
    
    for j in range(idx-1,i-1,-1):
        arr[j], arr[j+1] = arr[j+1], arr[j]
        ans += 1
print(ans)