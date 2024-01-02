n,m = map(int,input().split())

a = [0] * 1000001
b = [0] * 1000001

idx = 1

for i in range(n):
    direct, times = input().split()
    
    for _ in range(int(times)):
        if direct == 'R':
            a[idx] = a[idx-1] + 1
        else:
            a[idx] = a[idx-1] - 1
        idx += 1

idx = 1
for i in range(m):
    direct, times = input().split()
    
    for _ in range(int(times)):
        if direct == 'R':
            b[idx] = b[idx-1] + 1
        else:
            b[idx] = b[idx-1] - 1
        idx += 1

cnt = 0
ans = -1
for i in range(1,1001):
    if a[i] == b[i]:
        cnt = i
        break

print(max(ans, cnt))