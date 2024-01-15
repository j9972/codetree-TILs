n = int(input())
info = list()
for i in range(n):
    x,y = map(int,input().split())
    info.append((x,y,i+1))


info.sort(key = lambda x : (x[0] , -x[1]))
for i in info:
    print(i[0],i[1],i[2])