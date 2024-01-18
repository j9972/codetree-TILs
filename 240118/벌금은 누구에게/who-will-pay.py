n,m,k = map(int,input().split())

d = [1] * 101
for i in range(m):
    d[int(input())] += 1

#print(d)

ans = -1
for i in d:
    if i >= k:
        ans += 1

if ans != -1:
    print(ans + 1)
else:
    print(ans)