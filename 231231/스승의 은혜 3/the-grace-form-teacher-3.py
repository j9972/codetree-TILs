n,b = map(int,input().split())

arr = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

ans = 0

for i in range(n):

    tmp = arr[:]
    
    sum_val = 0
    budget = b

    element = tmp[i]
    tmp[i] = (element[0]//2, element[1])
    tmp.sort(key = lambda x: (x[0], x[1]))
        
    for i in tmp:
        p,d = i

        if budget < p + d:
            break
        
        sum_val += 1
        budget -= p + d

    ans = max(ans, sum_val)
print(ans)