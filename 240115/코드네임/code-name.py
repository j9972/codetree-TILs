students = []
for i in range(5):
    a,b = input().split()
    students.append((a,int(b)))

idx = 0
min_val = students[0][1]
for i in range(1,5):
    if students[i][1] < min_val:
        min_val = students[i][1]
        idx = i
print(students[idx][0], students[idx][1])