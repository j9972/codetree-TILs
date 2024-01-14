n,m,c = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

max_val = 0
a = list()

def interact(a,b,c,d):
    return not ((b < c) or (d < a))

def find_max_sum(cur_cnt, cur_weight, cur_val):
    global max_val

    if cur_cnt == m:
        if cur_weight <= c:
            max_val = max(max_val, cur_val)
        return

    find_max_sum(cur_cnt+1, cur_weight, cur_val)
    find_max_sum(cur_cnt+1, cur_weight + a[cur_cnt], cur_val + a[cur_cnt] ** 2)


def find_max(x,y):
    global a, max_val

    a = arr[x][y:y+m]

    max_val = 0
    find_max_sum(0,0,0)
    return max_val

def possible(x1,y1,x2,y2):
    if y1 + m -1 >= n or y2 + m -1 >= n:
        return False

    if x1 != x2:
        return True
    
    if interact(y1, y1+m-1, y2, y2+m-1):
        return False
    
    return True

ans = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            for h in range(n):
                if possible(i,j,k,h):
                    ans = max(ans, find_max(i,j) + find_max(k,h))
print(ans)