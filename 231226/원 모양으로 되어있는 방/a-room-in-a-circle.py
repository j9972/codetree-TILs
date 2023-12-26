import sys

n = int(input())
ppl = [
    int(input())
    for _ in range(n)
]

extend = ppl + ppl
ans = sys.maxsize

for i in range(n):
    sum_val = 0
    for j in range(i+1,i+n):
        sum_val += (j-i) * extend[j]
    ans = min(ans, sum_val)
print(ans)