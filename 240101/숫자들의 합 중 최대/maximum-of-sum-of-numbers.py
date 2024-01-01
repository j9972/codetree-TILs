x,y = map(int,input().split())

max_val = 0
for i in range(x,y+1):
    val = 0
    for j in str(i):
        val += int(j)
    
    max_val = max(max_val, val)
print(max_val)