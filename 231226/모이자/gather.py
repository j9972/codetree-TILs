import sys
min_value = sys.maxsize

n = int(input())
each = list(map(int,input().split()))

for i in range(n):
    sum_value = 0
    for j in range(n):
        if i == j:
            continue
        sum_value += abs(j-i) * each[j]
        
    min_value = min(min_value, sum_value)
print(min_value)