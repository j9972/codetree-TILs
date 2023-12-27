n, s = map(int,input().split())
values = list(map(int,input().split()))

res = list()

total = sum(values)

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        res.append(abs(s - (total - values[i] - values[j])))
        
print(min(res))