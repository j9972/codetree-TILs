n = int(input())

d = [0] * (101)

for i in range(n):
    idx, string = input().split()
    d[int(idx)] = 1 if string == 'G' else 2
    
max_value = 0
for i in range(101):
    for j in range(i+1,101):

        if d[i] == 0 or d[j] == 0:
            continue

        g,h = 0,0

        for k in range(i,j+1):
            if d[k] == 2:
                h += 1
            elif d[k] == 1:
                g += 1
        
        if h == g:
            max_value = max(max_value, j - i)

print(max_value)