n = int(input())

arr = [
    int(input())
    for _ in range(n)
]

max_val = 0
for i in range(1,1001):
    cnt = 0

    if arr[0] >= i:
        cnt += 1
    
    for j in range(1,n):
        if arr[j] > i and arr[j-1] <= i:
            cnt += 1
    
    max_val = max(max_val, cnt)
print(max_val)