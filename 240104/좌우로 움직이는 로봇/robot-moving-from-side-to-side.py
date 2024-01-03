n,m = map(int,input().split())

a,b = [0] * 1000001, [0] * 1000001

adx = 1
for _ in range(n):
    t,d = input().split()
    for i in range(int(t)):
        a[adx] = a[adx-1] + (1 if d == 'R' else -1)
        adx += 1

bdx = 1
for _ in range(m):
    t,d = input().split()
    for i in range(int(t)):
        b[bdx] = b[bdx-1] + (1 if d == 'R' else -1)
        bdx += 1

if adx > bdx:
    for i in range(bdx,adx):
        b[i] = b[i-1]
elif adx < bdx:
    for i in range(adx,bdx):
        a[i] = a[i-1]

ans = 0
maxTime = max(adx,bdx)
for i in range(1,maxTime):
    #print(a[i],':',b[i])
    if a[i] == b[i] and a[i-1] != b[i-1]:
        ans += 1
print(ans)