n,c,g,h = map(int,input().split())

equi = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

def temperature(low, high, t):
    if t < low:
        return c
    elif low <= t <= high:
        return g
    elif t > high:
        return h

# 특정 온도에 대해서 합
def cal(t):
    total = 0
    for a,b in equi:
        total += temperature(a,b,t)

    return total

max_val = 0
for i in range(1001):
    max_val = max(max_val, cal(i))
print(max_val)