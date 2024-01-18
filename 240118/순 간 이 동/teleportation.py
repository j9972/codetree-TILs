a,b,x,y = map(int,input().split())

print(min(abs(a-b), abs(x-a) + abs(b-y), abs(x-b) + abs(a-y)))