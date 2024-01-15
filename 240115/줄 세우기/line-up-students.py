n = int(input())

info = []
for i in range(n):
    h,w = map(int,input().split())
    info.append((h,w,i+1))

info.sort(key = lambda x : (-x[0],-x[1]))

for i in info:
    print(i[0],i[1],i[2])