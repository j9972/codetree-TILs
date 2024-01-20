a = list(map(int,input().split()))
a.sort()

max_dist = 0
for i in range(2):
    max_dist = max(max_dist, a[i+1] - a[i])

print(max_dist - 1)