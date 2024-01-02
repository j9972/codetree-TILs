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

idxb = 1
for i in range(m):
    direct, times = input().split()
    
    for _ in range(int(times)):
        if direct == 'R':
            b[idxb] = b[idxb-1] + 1
        else:
            b[idxb] = b[idxb-1] - 1
        idxb += 1

ans = -1
for i in range(1,idx):
    if a[i] == b[i]:
        ans = i
        break

print(ans)