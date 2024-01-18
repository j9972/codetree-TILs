n,m = map(int,input().split())

A = [0] * 1000001
B = [0] * 1000001

idx = 0
for i in range(n):
    v,t = map(int,input().split())

    for _ in range(t):
        A[idx] = A[idx-1] + v
        idx +=1

bidx = 0
for i in range(m):
    v,t = map(int,input().split())

    for _ in range(t):
        B[bidx] = B[bidx-1] + v
        bidx +=1

winner = 0
ans = 0
for i in range(idx):
    #print("before " , winner)
    if A[i] > B[i]:
        if winner == 0 or winner == 2:
            ans += 1
        winner = 1
    elif A[i] < B[i]:
        if winner == 0 or winner == 1:
            ans += 1
        winner = 2
    #print("after " , winner)
    elif A[i] == B[i]:
        if winner == 1 or winner == 2:
            ans += 1
        winner = 0
print(ans)