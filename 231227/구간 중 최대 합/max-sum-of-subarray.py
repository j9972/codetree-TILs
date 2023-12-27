n,k = map(int,input().split())
arr = list(map(int,input().split()))

max_value = 0
for i in range(n-k):
    sum_value = 0
    for j in range(k):
        sum_value += arr[i+j]
    max_value = max(max_value, sum_value)
print(max_value)