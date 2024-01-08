from collections import defaultdict

n, k = map(int, input().split())
arr = list(map(int, input().split()))
res = 0

for i in range(n-2):
    tmp_sum = k - arr[i]

    m = defaultdict(int)
    for j in range(i+1, n):
        res += m[tmp_sum - arr[j]]
        m[arr[j]] += 1
print(res)