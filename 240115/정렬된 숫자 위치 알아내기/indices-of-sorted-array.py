n = int(input())
info = list(map(int,input().split()))

tmp = []
for i in range(n):
    tmp.append((info[i],i))

new = tmp[:]
#print(new)
tmp.sort()
#print(tmp)

ans = []
for _, data in enumerate(new):
    for j, val in enumerate(tmp):
        if data == val:
            ans.append(j+1)
print(*ans)