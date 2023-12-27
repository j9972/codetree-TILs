import sys

n, s = map(int,input().split())
values = list(map(int,input().split()))
total = sum(values)

min_val = sys.maxsize
for i in range(n):
    for j in range(n):
        if i == j:
            continue
            
        min_val = min(min_val, abs(total - values[i] - values[j]))

print(abs(s - min_val))