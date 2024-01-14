n,m,c = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

max_val = 0
a = list()

def interact(x1,y1,x2,y2):
    return not ((y1 < x2) or (y2 < x1))

def find_max_sum(cur_idx, cur_weight, cur_val):
    global max_val

    if cur_idx == m:
        if cur_weight <= c:
            max_val = max(max_val, cur_val)
        return

    find_max_sum(cur_idx+1, cur_weight, cur_val)
    find_max_sum(cur_idx+1, cur_weight + a[cur_idx], cur_val + a[cur_idx] ** 2)

def find_max(x1,y1):
    global a, max_val

    a = arr[x1][y1:y1+m]

    max_val = 0
    find_max_sum(0,0,0)
    return max_val

def possible(x1,y1,x2,y2):
    if y1 + m - 1 >= n or y2 + m - 1 >= n:
        return False

    if x1 != x2:
        return True
    
    if interact(y1, y1+m-1, y2,y2+m-1):
        return False
    
    return True

ans = 0
for x1 in range(n):
    for y1 in range(n):
        for x2 in range(n):
            for y2 in range(n):
                if possible(x1,y1,x2,y2):
                    ans = max(ans, find_max(x1,y1) + find_max(x2,y2))
print(ans)