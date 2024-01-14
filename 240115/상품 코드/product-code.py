class User:
    def __init__(self, name="codetree", code=50):
        self.name = name
        self.code = code


# 변수 선언 및 입력
name, code = tuple(input().split())
u = User()

print("product {} is {}".format(u.code, u.name))

u = User(name, code)

print("product {} is {}".format(u.code, u.name))