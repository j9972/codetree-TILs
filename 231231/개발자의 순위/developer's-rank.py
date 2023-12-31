k, n = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(k)
]

ans = 0

for i in range(n):
    for j in range(n):

        if i == j:
            continue
        
        f = True

        for data in arr: # 한번이라도 순위가 바뀌면 버린다
            ii = data.index(i+1)
            jj = data.index(j+1)

            if ii > jj:
                f = False
        
        if f:
            ans += 1
print(ans)