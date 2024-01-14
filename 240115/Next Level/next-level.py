class Student:
    def __init__(self, id_="codetree", level=10):
        self.id_ = id_
        self.level = level

# 변수 선언 및 입력
id_, level = tuple(input().split())

s = Student()
# 출력
print(f"user {s.id_} lv {s.level}")
s = Student(id_, level)
print(f"user {s.id_} lv {s.level}")