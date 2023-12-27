n,k = map(int,input().split())

d = [0] * (10001)
max_idx = 0
min_idx = 10001

for i in range(n):
    idx, string = input().split()
    val = 0
    if string == 'G':
        val = 1
    else:
        val = 2
    max_idx = max(max_idx,int(idx))
    min_idx = min(min_idx,int(idx))
    d[int(idx)] = val

# for i in range(min_idx,max_idx+k):
#     print(d[i], end= ' ')

max_value = 0
for i in range(min_idx,max_idx+k):
    sum_value = 0
    for j in range(k+1):
        sum_value += d[i+j]
    max_value = max(max_value,sum_value)

print(max_value)