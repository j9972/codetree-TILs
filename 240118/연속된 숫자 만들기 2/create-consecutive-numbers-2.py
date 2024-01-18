a = list(map(int,input().split()))
a.sort()

if a[0] + 1 == a[1] and a[1] + 1 == a[2]:
    print(0)
elif a[0] + 2 == a[1] or a[1] + 2 == a[2]:
    print(1)
else:
    print(2)