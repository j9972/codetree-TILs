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

bad_cheese = [0] * (d+1)

time_idx = 1
for i in range(100):
    for sick_person, sick_time in sick: # sick_time == 3 or 8
        for j in range(time_idx,sick_time):
            for person, cheese, eat_time in eat_ppl:
                if sick_time >= eat_time >= time_idx and sick_person == person:
                    bad_cheese[cheese] += 1
        time_idx = sick_time
#print(bad_cheese)

box = []
for i in range(len(bad_cheese)):
    if bad_cheese[i] == max(bad_cheese):
        box.append(i)

res = set()
for person, cheese, eat_time in eat_ppl: 
    if cheese in box:
        res.add(person)
print(len(res))