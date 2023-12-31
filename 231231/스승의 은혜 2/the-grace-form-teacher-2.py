n,b = map(int,input().split())
price = [
    int(input())
    for _ in range(n)
]

ans = 0

for i in range(n):
    t = price[:]
    bb=b

    t[i] //= 2
    t.sort()
    
    sum_val = 0
    for i in t:
        if bb < i:
            break

        sum_val += 1
        bb -= i
        
    ans = max(ans, sum_val)
print(ans)