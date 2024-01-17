n,m = map(int,input().split())

DA = [0] * 1000001
DB = [0] * 1000001

a_idx = 1
for i in range(n):
    d,t = input().split()
    t = int(t)

    for _ in range(t):
        if d == 'R':
            DA[a_idx] = DA[a_idx-1] + 1
        else:
            DA[a_idx] = DA[a_idx-1] - 1
        a_idx += 1


b_idx = 1
for i in range(m):
    d,t = input().split()
    t = int(t)

    for _ in range(t):
        if d == 'R':
            DB[b_idx] = DB[b_idx-1] + 1
        else:
            DB[b_idx] = DB[b_idx-1] - 1
        b_idx += 1

ans = -1
for i in range(1,a_idx):
    if DA[i] == DB[i]:
        ans = i
        break

print(ans)