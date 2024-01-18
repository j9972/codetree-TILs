n,m,k = map(int,input().split())

d = [0] * 101
for i in range(m):
    d[int(input())] += 1

#print(d)

ans = -1
for i in range(101):
    if d[i] >= k:
        ans = i
        break

print(ans)