n,m = map(int,input().split())

A = [0] * 1000001
B = [0] * 1000001

idx = 0
for i in range(n):
    t,d = input().split()
    t = int(t)

    for _ in range(t):
        if d == 'R':
            A[idx] = A[idx-1] + 1
        elif d == 'L':
            A[idx] = A[idx-1] - 1
        idx += 1

b_idx = 0
for i in range(m):
    t,d = input().split()
    t = int(t)

    for _ in range(t):
        if d == 'R':
            B[b_idx] = B[b_idx-1] + 1
        elif d == 'L':
            B[b_idx] = B[b_idx-1] - 1
        b_idx += 1

if idx > b_idx:
    for i in range(b_idx,idx+1):
        B[i] = B[b_idx]
elif idx < b_idx:
    for i in range(idx,b_idx+1):
        A[i] = A[idx]

ans = 0
for i in range(1,max(idx,b_idx)):
    if A[i-1] != B[i-1]:
        if A[i] == B[i]:
            ans += 1
print(ans)