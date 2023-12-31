n, k = map(int,input().split())

boom = [
    int(input())
    for _ in range(n)
]

max_val = -1

for i in range(n):
    for j in range(n):
        if i == j:
            continue

        if abs(i-j) <= k and boom[i] == boom[j]:
            max_val = max(max_val, boom[i])
print(max_val)