from itertools import combinations as cb

n,m = map(int,input().split())

a = [
    input()
    for _ in range(n)
]

b = [
    input()
    for _ in range(n)
]

numList = list(range(0,m))

ans = 0
for num in cb(numList,3):
    aset = set()
    bset = set()

    for i in range(n):
        string1 = ""
        string2 = ""

        for k in num:
            string1 += a[i][k]
            string2 += b[i][k]
        
        aset.add(string1)
        bset.add(string2)
    
    alen = len(aset)
    blen = len(bset)    

    if len(aset | bset) == alen + blen:
        ans += 1
print(ans)