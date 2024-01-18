a = list(map(int,input().split()))
a.sort()

print(min(a[1] - a[0], a[2] - a[1]) - 1)