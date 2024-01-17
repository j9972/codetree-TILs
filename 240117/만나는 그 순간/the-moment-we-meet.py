n,m = map(int,input().split())

DA = [0] * 1001
DB = [0] * 1001

a_idx = 1
for i in range(n):
    d,t = input().split()
    t = int(t)

    for j in range(a_idx, a_idx+t):
        if d == 'R':
            DA[j] = DA[j-1] + 1
        else:
            DA[j] = DA[j-1] - 1
    a_idx += t

b_idx = 1
for i in range(m):
    d,t = input().split()
    t = int(t)

    for j in range(b_idx, b_idx+t):
        if d == 'R':
            DB[j] = DB[j-1] + 1
        else:
            DB[j] = DB[j-1] - 1
    b_idx += t

for i in range(a_idx,max(a_idx,b_idx)+1):
    DA[i] = DA[a_idx-1]
for i in range(b_idx,max(a_idx,b_idx)+1):
    DB[i] = DB[b_idx-1]

ans = -1
for i in range(1,max(a_idx,b_idx)+1):
    if DA[i] == DB[i]:
        ans = i
        break
print(ans)