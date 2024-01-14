# students = []
# for i in range(5):
#     a,b = input().split()
#     students.append((a,int(b)))

# idx = 0
# min_val = students[0][1]
# for i in range(1,5):
#     if students[i][1] < min_val:
#         min_val = students[i][1]
#         idx = i
# print(students[idx][0], students[idx][1])

class User:
    def __init__(self, code_name, score):
        self.code_name = code_name
        self.score = score


# 변수 선언 및 입력
users = []

for _ in range(5):
    code_name, score = tuple(input().split())
    users.append(User(code_name, int(score)))

min_idx = 0
for i in range(1,5):
    if users[min_idx].score > users[i].score:
        min_idx = i

print(users[min_idx].code_name, users[min_idx].score)