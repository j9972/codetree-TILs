h1,m1,h2,m2 = map(int,input().split())

elapsed_time = 0

while True:
    if h1 == h2 and m1 == m2:
        break

    elapsed_time += 1
    m1 += 1

    if m1 == 60:
        h1 += 1
        m1 = 0

print(elapsed_time)