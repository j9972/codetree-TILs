import sys

n = int(input())
arr = list(map(int,input().split()))

ans = -sys.maxsize
for i in range(n):
    for j in range(n):
        sum_val = arr[i]
        if i-1 <= j <= i+1:
            continue
        sum_val += arr[j]
        ans = max(ans, sum_val)
print(ans)