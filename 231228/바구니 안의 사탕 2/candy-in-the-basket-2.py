n,k = map(int,input().split())

d = [0] * 101
for i in range(n):
    cnt,idx = map(int,input().split())
    d[idx] += cnt

max_cnt = 0
for c in range(100):
    sum_cnt = 0
    for i in range(c-k,c+k+1):
        if 0 <= i <= 100:
            sum_cnt += d[i]
    
    max_cnt = max(max_cnt, sum_cnt)
print(max_cnt)