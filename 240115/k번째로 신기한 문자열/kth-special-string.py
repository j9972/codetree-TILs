n,k,string = input().split()

length = len(string)

res = []
for i in range(int(n)):
    data = input()
    if data[:length] == string:
        res.append(data)

res.sort()

print(res[int(k)-1])