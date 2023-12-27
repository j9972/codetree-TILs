from itertools import permutations as pm

n,m = map(int,input().split())

a = tuple(map(int,input().split()))
b = tuple(map(int,input().split()))

new = list(pm(b,len(b)))
cnt = 0

for i in range(n-m+1):
    val = a[i:i+m]
    
    if val in new:
        cnt += 1
print(cnt)