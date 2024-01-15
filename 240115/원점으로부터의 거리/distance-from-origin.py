n = int(input())
info = list()
for i in range(n):
    x,y = map(int,input().split())
    info.append((x,y,i+1))


info.sort(key = lambda x : (abs(x[0]) + abs(x[1]), x[2] ))
for i in info:
    print(i[2])