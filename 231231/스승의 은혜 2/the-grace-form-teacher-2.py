n,b = map(int,input().split())
price = [
    int(input())
    for _ in range(n)
]

ans = 0

for i in range(n):
    t = price[:]

    t[i] //= 2
    t.sort()
    
    sum_val = 0
    for i in t:
        if b < i:
            break
        sum_val += 1
        b -= i

    ans = max(ans, sum_val)
print(ans)