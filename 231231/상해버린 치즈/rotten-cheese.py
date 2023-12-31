n,m,d,s = map(int,input().split())

eat_ppl = [
    tuple(map(int,input().split()))
    for _ in range(d)
]

eat_ppl.sort(key=lambda x : x[2])

sick = [
    tuple(map(int,input().split()))
    for _ in range(s)
]

sick.sort(key=lambda x : x[1])

cheese = [0] * (m+1)

for i in range(d):
    p,badCheese,t = eat_ppl[i]

    for j in sick:
        sickPerson, fromWhen = j

        if t < fromWhen and p == sickPerson:
            cheese[badCheese] += 1
            
possible = list()
for i, v in enumerate(cheese):
    if v == max(cheese):
        possible.append(i)

ans = set()
for i in eat_ppl:
    person, bad, _ = i
    if bad in possible:
        ans.add(person)
        
print(len(ans))