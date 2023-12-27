import sys

n, s = map(int,input().split())
values = list(map(int,input().split()))

values.sort()

total = sum(values)

if total <= s:
    print(s - (total - values[0] - values[1]))
else:
    min_val = sys.maxsize

    for i in range(n):
        for j in range(n):

            if i == j:
                continue
            
            min_val = min(min_val, abs(total - values[i] - values[j]))
            

    print(abs(min_val - s))