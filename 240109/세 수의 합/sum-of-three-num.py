from collections import defaultdict

n, k = map(int, input().split())
arr = list(map(int, input().split()))
res = 0

count = defaultdict(int)

for e in arr:
    if e in count:
        count[e] += 1
    else:
        count[e] = 1

for i in range(n):
    count[arr[i]] -= 1 # 중복방지를 위해 지움
    for j in range(i):
        diff = k - arr[i] - arr[j]
        if diff in count:
            res += count[diff]
print(res)