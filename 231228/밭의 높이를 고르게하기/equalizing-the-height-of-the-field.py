import sys

n,h,t = map(int,input().split())
arr = list(map(int,input().split()))

# h과 가장 가까운것들 먼저 찾기
check_list = list()
for i in arr:
    check_list.append(abs(h-i))

#print(check_list)

ans = sys.maxsize
for i in range(n-t+1):
    sum_val = 0
    for j in range(i,i+t):
        sum_val += check_list[j]
    
    ans = min(ans, sum_val)
print(ans)