n = int(input())

arr = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

ans = 0
select = list()

def possible():
    for idx1, val1 in enumerate(select):
        for idx2, val2 in enumerate(select):
            x1,y1 = val1
            x2,y2 = val2

            if idx1 < idx2 and ((x1<=x2<=y1) or (x1<=y2<=y1) or (x2<=x1<=y2) or (x2<=y1<=y2)):
                return False
    return True

def choose(cnt, num):
    global ans
    if cnt > n or num > n:
        return
    
    if possible():
        ans = max(ans, len(select))
    
    for i in range(num,n):
        select.append(arr[i])
        choose(cnt+1, i+1)
        select.pop()
        
choose(0,0)
print(ans)

# arr.sort()

# d = [0] * 1001
# cnt = 0

# for x1,x2 in arr:
#     flag = False
    
#     for j in range(x1,x2+1):
#         if d[j] == 1:
#             flag = True
#             break
#         d[j] = 1

#     if flag == False:
#         cnt += 1
# print(cnt)