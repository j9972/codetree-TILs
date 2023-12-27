n,k = map(int,input().split())

d = [0] * (10001)
max_idx = 0
min_idx = 10001

for i in range(n):
    idx, string = input().split()
    d[int(idx)] = 1 if string == 'G' else 2
    max_idx = max(max_idx,int(idx))
    min_idx = min(min_idx,int(idx))
    

max_value = 0
for i in range(min_idx,max_idx+k):
    sum_value = 0
    for j in range(k+1):
        if i+j <= 10000:
            sum_value += d[i+j]
        else:
            break
    max_value = max(max_value,sum_value)

print(max_value)