n = int(input())
arr = list(map(int,input().split()))

max_val = 0
for d in range(1,101):
    val = 0
    for i in range(n):
        for j in range(i+1,n):
            if arr[j] - d == d - arr[i]:
                val += 1
    max_val = max(max_val, val)

print(max_val)